from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import pandas as pd
import json
import os 

load_dotenv() 
mongo_key = os.getenv("MongoDB")

uri = f"mongodb+srv://harsharya1004:{mongo_key}@cluster0.llygeds.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)

class mongodb_operation:
    def __init__(self, client_url: str, database_name: str):
        self.client_url = client_url
        self.database_name = database_name
    
    def create_client(self):
        client = MongoClient(self.client_url)
        return client
    
    def create_database(self):
        client = self.create_client()
        database = client[self.database_name]
        return database

    def create_collection(self, collection_name: str=None):
        database = self.create_database()
        collection = database[collection_name]
        return collection

    def insert_record(self, record, collection_name: str):
        collection = self.create_collection(collection_name)

        if type(record) == dict:
            collection.insert_one(record)

        elif type(record) == list:
            for data in record:
                if type(data) != dict:
                    raise TypeError("Record must be in dictionary")
            collection.insert_many(record)

    def bulk_insert(self, filepath: str, collection_name: str=None):
        if filepath.endswith('.csv'):
            data = pd.read_csv(filepath, encoding = 'utf-8')
        elif filepath.endswith('.xlsx'):
            data = pd.read_excel(filepath, encoding='utf-8')
        datajson = json.loads(data.to_json(orient='records'))
        collection = self.create_collection()
        collection.insert_many(datajson)
         
        