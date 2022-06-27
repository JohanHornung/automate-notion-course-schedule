# lecture Data Object for Notion DB entry
class Lecture:

    def __init__(
        self, 
        begin_date: str, 
        end_date: str,
        begin_time: str, 
        end_time: str, 
        lecturer: str,
        topic: str,
        room: int,
        type: str) -> None:
        
        self.begin_date = begin_date
        self.end_date = end_date
        self.begin_time = begin_time
        self.end_time = end_time
        self.lecturer = lecturer
        
        self.topic = topic
        # special topic filter
        self.EXAMS = [
            "Präsentation Praxisbericht 1. Studienjahr", 
            "Wissenschaftliches Arbeiten, Methoden- und Sozialkompetenz"
        ]

        self.room = room
        self.type = type
        # page data will conform to the parent db property data schema
        self.data = {}

    # method selects the corresponding data item of a list of options
    def select_from_options(self, attribute: str, options: list[dict[str, str]]) -> dict[str, str]:
        found = False
        right_option = {}
        
        # getting attribute from instance
        attribute_value = getattr(self, attribute)
        # searching for corresponding option
        for option in options:
            if str(attribute_value) == option["name"]:
                right_option = option
                found = True
        
        # searching in special topics if no entry has been found yet 
        if not found:
            for special_topic in self.EXAMS:
                if str(attribute_value) == special_topic:
                    found = True
                    # TODO: create entry for edge cases
        
        # if there is still no valid option found
        if not found:
            print("No match.")
             
        # returning data object
        return right_option
    
    # TODO: method checks for completeness of the information in the lecture object
    def is_complete() -> bool:
        pass