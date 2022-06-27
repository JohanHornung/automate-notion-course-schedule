NOTION_INTEGRATION_TOKEN = "secret_9Vv9Jvzubn3V15iczlRICd3774WL5TtOjN1YOksuSwq"
NOTION_DATABASE_ID = '00f8a439d43643dea57682676a622ce2'

NOTION_DB_PROPERTY_TEMPLATE = {
    "parent": {
        "database_id": NOTION_DATABASE_ID
    },
    "properties": {
        'Lecture': {
            'title': [
                {
                    'text': {
                        'content': '',
                        },
                }
            ]
        },
        "Dates": {
            # "id": "0%23%7Dp",
            # "name": "Dates",
            # "type": "date",
            "date": {
            # placeholder
                "start": "",
                "end": "",
            }
        },
        "Lecturer": {
            # "id": "_%5B%3Da", 
            # "name": "Lecturer",
            # "type": "select",
            "select": {
                'options': [
                    {
                        'name': 'Group Work',
                    },
                    {
                        'name': 'Jürgen Rolf', 
                    },
                    {
                        'name': 'Dr. René Rüth', 
                    },
                    {
                        'name': 'Prof. Dr. Volker Drosse', 
                    },
                    {
                        'name': 'Jennifer King', 
                    },
                    {
                        'name': 'Prof. Dr. Matthias Maßmann', 
                    }
                    ]
                }
        },
        "Type": {
            # "id": "f%5E%5E%3B",
            # "name": "Type",
            # "type": "select",
            "select": {
                # placeholder
                "options": [
                    {
                        "name": "Project Blocker 💭💭💭",
                    },
                    {
                        "name": "Course 📙📙📙",   
                    },
                    {
                        "name": "Exam ✏️✏️✏️",   
                    }
                ]
            }
        },
        "Room": {
            # "id": "qy%7B%7B",
            # "name": "Room",
            # "type": "number",
            # placeholder
            "number": 0
        },
        "Topic": {
            # "id": "v%3CK%5D",
            # "name": "Topic",
            # "type": "select",
            "select": {
                # placeholder
                "options": [
                    {
                        'name': 'Übungen/Projektgruppen',
                    },
                    {
                        "name": "General Management II",   
                    },
                    {
                        "name": "Statistik",   
                    },
                    {
                        "name": "Prog. Design und Implementierung von Algorithmen II",   
                    },
                    {
                        "name": "Business English II",   
                    },
                    {
                        "name": "Accounting",   
                    },
                    {
                        "name": "Formale Grundlagen der Informatik",   
                    }
                ]
            }
        }
    }
}
    
