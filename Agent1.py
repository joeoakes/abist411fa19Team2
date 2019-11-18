
import sys, json, urllib.request, ssl, socket, datetime
from pymongo import MongoClient

# Project App 1
# Purpose: retrieve JSON paylaod and send it with TLS to App 2

def retrievePayload():
 response = urllib.request.urlopen(url+param)
 payload = response.read()
 return payload


#CURL
url='https://jsonplaceholder.typicode.com'
param='/posts/1'

try:
 #response = urllib.request.urlopen(url+param)
 #payload = response.read()

 payload = retrievePayload()

 #SSL/TLS connection
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 ssl_sock = ssl.wrap_socket(s, ca_certs="server.crt", cert_reqs=ssl.CERT_REQUIRED)
 ssl_sock.connect(('localhost',8080))


 #Payload Send
 ssl_sock.sendall(payload)
 print("sending complete")

 #Decode and save in a JSON file
 payloadJSON = json.loads(payload.decode('utf-8'))
 with open('payload.json', 'w') as outFile:
        jsonApp = outFile.write(json.dumps(payloadJSON))


 #saving workflow action
 client = MongoClient('localhost', 27017)
 db = client.Team2
 collection = db.agent1
 print("Saved workflow action")
 post_id = collection.insert({"action" : "Payload Sent", "time" : datetime.datetime.now()})



except Exception as e:
 print(e)
 print(ssl_sock.cipher())
 ssl_sock.close()

