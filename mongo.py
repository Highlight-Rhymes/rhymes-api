# import json
# from pymongo import MongoClient

from flask import Flask
from pymongo import MongoClient
from constants import *

client = MongoClient('mongodb://rhymes-db:27017/')
db = client.rhymes

def insertSong(song):
    songsCollection = db.songs
    return songsCollection.insert({"song": song}).inserted_id

def getSongs():
    songsCollection = db.songs
    cursor = songsCollection.find({})
    songs = []
    for document in cursor:
        songs.append({ "id": str(document["_id"]), "song": document["song"] })
    return songs
    # songs = getDB()['songs']
    # cursor = songs.find({})
    # total = []
    # for document in cursor:
    #     total.append({ "id": str(document["_id"]), "song": document["song"] })
    # return total