# import json
# from pymongo import MongoClient

from flask import Flask
from flask_pymongo import PyMongo
from constants import *
app = Flask(__name__)
app.config["MONGO_URI"] = MONGODB_URI_TEST
mongo = PyMongo(app)

# def getDB():
#     client = MongoClient('localhost', 27017)
#     return mongo['rhymes']

def insertSong(song):
    # return getDB()['songs'].insert_one({"song": song}).inserted_id
    return mongo['songs'].insert_one({"song": song}).inserted_id

def getSongs():
    songs = getDB()['songs']
    cursor = songs.find({})
    total = []
    for document in cursor:
        total.append({ "id": str(document["_id"]), "song": document["song"] })
    return total