import json
from pymongo import MongoClient

def getDB():
    client = MongoClient('localhost', 27017)
    return client['rhymes']

def insertSong(song):
    return getDB()['songs'].insert_one({"song": song}).inserted_id

def getSongs():
    songs = getDB()['songs']
    cursor = songs.find({})
    total = []
    for document in cursor:
        total.append({ "id": str(document["_id"]), "song": document["song"] })
    return total