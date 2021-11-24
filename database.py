from datetime import date
from pprint import pprint
from pymongo import MongoClient
import os, datetime, uuid

mongo_client = MongoClient(os.environ["MONGODB"])
mongo_db = mongo_client['TaskManagerDB']
mongo_collection_tasks = mongo_db['Tasks']

class database:

    def initialize_db():
        if "Tasks" not in mongo_db.list_collection_names():
            mongo_collection_tasks.insert_one({
                "taskid": str(uuid.uuid4()),
                "name": "Test Task 1", 
                "description": "Description of Test Task 1", 
                "due": datetime.datetime.utcnow() + datetime.timedelta(days=20),
                "completed": False,
                "created": datetime.datetime.utcnow(),
                "modified": datetime.datetime.utcnow()
                })
            mongo_collection_tasks.insert_one({ 
                "taskid": str(uuid.uuid4()),
                "name": "Test Task 2", 
                "description": "Description of Test Task 2", 
                "due": datetime.datetime.utcnow() + datetime.timedelta(days=30),
                "completed": False,
                "created": datetime.datetime.utcnow(),
                "modified": datetime.datetime.utcnow()
                })
            mongo_collection_tasks.insert_one({ 
                "taskid": str(uuid.uuid4()),
                "name": "Test Task 3", 
                "description": "Description of Test Task 3", 
                "due": datetime.datetime.utcnow() + datetime.timedelta(days=40),
                "completed": False,
                "created": datetime.datetime.utcnow(),
                "modified": datetime.datetime.utcnow()
                })
            mongo_collection_tasks.insert_one({ 
                "taskid": str(uuid.uuid4()),
                "name": "Test Task 4", 
                "description": "Description of Test Task 4", 
                "due": datetime.datetime.utcnow() + datetime.timedelta(days=50),
                "completed": False,
                "created": datetime.datetime.utcnow(),
                "modified": datetime.datetime.utcnow()
                })

    def find_tasks(starting_point):
        tasks = []
        for task in mongo_collection_tasks.find(skip=starting_point, limit=10):
            tasks.append(task)
        return tasks

    def find_task(task_id):
        return mongo_collection_tasks.find_one({"taskid": task_id})

    def update_task(data):
        data['modified'] = datetime.datetime.utcnow()
        return mongo_collection_tasks.update({"taskid": data['taskid']}, data)