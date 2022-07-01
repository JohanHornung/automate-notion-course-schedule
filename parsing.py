import copy
import secrets
from lecture import *


# special topic filter
EXAMS = [
    "Präsentation Praxisbericht 1. Studienjahr", 
    "Wissenschaftliches Arbeiten, Methoden- und Sozialkompetenz"
]

# opening and parsing schedule csv file 
def parse_schedule_file(filepath: str) -> list[str]:
    print("Parsing .csv schedule file entries...\n")
    # .csv seperator for splitting rows in file
    global seperator
    seperator = ';'
    # collection of courses
    schedule_data = []
    with open(filepath, encoding="utf-8", mode="r") as schedule_file:
        # going through each entry (except the column names)
        for lecture in list(schedule_file)[1:]:
            schedule_data.append([elem for elem in lecture.split(seperator)[:-1]]) # removing new lines
        # "begin_date, begin_time, end_time, topic, lecturer, room" in this order
        
    return schedule_data

# parsing schedule data entries to data page object (for notion page creation)
def parse_schedule_data(schedule_data: list[str]) -> list[Lecture]:
    print("Parsing schedule data...\n")
    pages = []
    
    for item in schedule_data:
        # making a new copy from the DB property template
        new_page = copy.deepcopy(secrets.NOTION_DB_PROPERTY_TEMPLATE)
        new_page_data = new_page["properties"]

        # changing date & time format: YYYY-MM-DDTHH:MM:SS.MMS+02:00
        start_date = item[0].replace(".", "-")
        # lectures will always be on the same day
        end_date = start_date
        # time
        start_time = item[1]
        end_time = item[2]

        # TODO: dynamic summer time
        # formatting date/time
        start_date_fmt = f"{start_date}T{start_time}:00.000+2:00" # summer time
        end_date_fmt = f"{end_date}T{end_time}:00.000+2:00"
        
        # additional lecture informations (topic and lecturer)
        topic = item[3]
        # treating special characters in lecturer names
        lecturer = item[4].replace("\xa0", " ") if item[4] != '' else 'Group Work'
        
        # room number if there is one or if it is not a virtual room
        room = item[5]
        room_number = 0 if room == '' or room[:2] == 'VR' else int(room)
        
        # TODO: implement logic and unhardcode lecture types
        type = "Exam ✏️✏️✏️" if topic in EXAMS else "Course 📙📙📙"  
        
        # creating Lecure object
        print("Creating Lecture instance...\n")
        lecture = Lecture(
            start_date, 
            end_date, 
            start_time, 
            end_time, 
            lecturer, 
            topic, 
            room, 
            type
        )
                
        # date/time
        new_page_data["Dates"]["date"]["start"] = start_date_fmt
        new_page_data["Dates"]["date"]["end"] = end_date_fmt
        
        # searching for corresponding lecturer
        attribute = "lecturer"
        options = new_page_data["Lecturer"]["select"]["options"]
        new_page_data["Lecturer"]["select"] = lecture.select_from_options(attribute, options)
 
        # searching for corresponding lecture type
        attribute = "type"
        options = new_page_data["Type"]["select"]["options"]
        new_page_data["Type"]["select"] = lecture.select_from_options(attribute, options)
        
        # room number
        new_page_data["Room"]["number"] = room_number

        # name/title
        title = topic # for now
        new_page_data["Lecture"]["title"][0]["text"]["content"] = title

        # searching for corresponding lecture topic
        attribute = "topic"
        options = new_page_data["Topic"]["select"]["options"]
        new_page_data["Topic"]["select"] = lecture.select_from_options(attribute, options)
        
        # TODO: find a way to get one drive/goodnotes links for protocols or scripts
        new_page_data["Script"]["files"] = [] # for now
        new_page_data["Protocol"]["files"] = [] # for now

        # adding lecture data to the lectures data attribute
        lecture.data = new_page
        # adding lecture object to collection
        pages.append(lecture)
        
    return pages

