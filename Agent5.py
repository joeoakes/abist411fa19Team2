import sys, json, urllib.request, ssl, socket, datetime
from pymongo import MongoClient

# Project App 5
# Purpose: mongo5 - logger for project diamond

try:
 #saving workflow action
 client = MongoClient('localhost', 27017)
 db = client.Team2
 collection = db.agent1
 print("Saved workflow action")
 post_id = collection.insert({"action" : "Payload Sent", "time" : datetime.datetime.now()})

except Exception as e:
 print(e)
