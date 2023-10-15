from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from dbscript import seedDB


app = FastAPI()
client  = MongoClient("mongodb://localhost:27017")
db = client["mycourses"]

if db["courses"].count_documents({}) == 0:
    seedDB()

