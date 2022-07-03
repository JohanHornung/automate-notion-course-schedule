import requests
import time
from parsing import *
import secrets

# pushing collection of data objects (Notion pages) into DB
def push(pages: list[Lecture]) -> str:
    print("Pushing data (lecture pages) to Notion DB...\n")
    
    # Notion DB API connection
    base_url = 'https://api.notion.com/v1/pages'
    header = {
        "Authorization": secrets.NOTION_INTEGRATION_TOKEN,
        "Notion-Version": "2022-02-22"
    }

    # pushing each new page entry to DB
    for page in pages:
        try:
            payload = {
                "parent": secrets.NOTION_DATABASE_ID,
                "properties": page.data["properties"]                
            }
            # print(payload)
            # making POST request to Notion API to push data
            response = requests.post(
                base_url, 
                json=payload,
                headers=header, 
            )
            # raising error if there´s one
            response.raise_for_status()
            print(response.json())
        # error handling
        except (
            requests.exceptions.HTTPError, 
            requests.exceptions.ConnectionError, 
            requests.exceptions.Timeout, 
            requests.exceptions.RequestException,
            requests.exceptions.InvalidJSONError
        ) as err:
            print(err)    
        
        # timeout
        time.sleep(2)




# entry point
def main():
    # parsing .csv file
    data = parse_schedule_file("data/studienplan_2_semester.csv")
    # parsing data to page objects
    pages = parse_schedule_data(data)
    # pushing pages to Notion DB
    push(pages)








if __name__ == "__main__":
    main()

