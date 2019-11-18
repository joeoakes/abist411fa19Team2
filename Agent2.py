#Agent 2

import socket, ssl, pysftp, json, hashlib, hmac, datetime
from pymongo import MongoClient

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts,'host':'oz-ist-linux-oakes','username':'ftpuser','password':'test1234','port':100}

try:
        print("create an INET, STREAMing socket using SSL")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssl_sock = ssl.wrap_socket(s,
                server_side=True,
                certfile="server.crt",
                keyfile="server.key")
        print("bind the socket to a public host, and a well-known port 8080")
        ssl_sock.bind(('localhost', 8080))
        ssl_sock.listen(5)
        print("ciphers: " + str(ssl_sock.cipher()))

        #saving workflow action
        client = MongoClient('localhost',27017)
        db = client.Team2
        collection =db.agent2
        print("Saved workflow action")
        post_id = collection.insert({"action": "Created connection", "time" : datetime.datetime.now()})


        while True:
                print("accept connections from outside")
                (clientsocket, address) = ssl_sock.accept()
                data = clientsocket.recv(1024)
                print(data)

                #verify the hash
                checksum = hashlib.sha256(data).hexdigest()
                print("SHA256: ", checksum)

                #decode the data
                payloadJSON = json.loads(data.decode('utf-8'))

                #Connect to sftpuser
                #Create a json file and send it to sftpuser
                with pysftp.Connection(**cinfo) as sftp:
                        print("Connection made")
                        with open ('payloadReceive.json', 'w') as outFile:
                                jsonPayload = outFile.write(json.dumps(payloadJSON))
                        print("Sending payloadReceive.json file to ftpuser")
                        sftp.put('payloadReceive.json')
except Exception as e:
        print(e)
        ssl_sock.close()



