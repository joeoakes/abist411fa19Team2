#Agent 2

import socket, ssl
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
        while True:
                print("accept connections from outside")
                (clientsocket, address) = ssl_sock.accept()
                print(clientsocket.recv(4096))
except Exception as e:
        print(e)
        ssl_sock.close()


