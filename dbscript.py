import pymongo
import json

def seedDB() -> None:
    '''seeds the database on first run'''
    client = pymongo.MongoClient("mongodb://localhost:27017")

    #get the database
    db = client["mycourses"]
    collection = db["courses"]

    #read courses.json
    with open('courses.json') as f:
        courses = json.load(f)

    #create index
    collection.create_index("name")

    for course in courses:
        course["rating"] = {"total": 0, "count": 0}
        for chapter in course["chapters"]:
            chapter["rating"] = {"total": 0, "count": 0}
        collection.insert_one(course)

    client.close()