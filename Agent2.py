#Agent 2

import socket, ssl
from pymongo import MongoClient
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
        client = MongoClient('localhost', 27017)
        db = client.Team2
        collection = db.agent2
        print("Saved workflow action")
        post_id = collection.insert({"action" : "Created connection"})

        while True:
                print("accept connections from outside")
                (clientsocket, address) = ssl_sock.accept()
                data = clientsocket.recv(1024)
                print(data)



except Exception as e:
        print(e)
        ssl_sock.close()


