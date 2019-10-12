import sys, json, urllib.request, ssl, socket


# Project App 1
# Purpose: retrieve JSON paylaod and send it with TLS to App 2

#CURL
url='https://jsonplaceholder.typicode.com'
param='/posts/1'

try:
 response = urllib.request.urlopen(url+param))
 payload = response.read()

 #SSL/TLS connection
 s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 ssl_sock = ssl.wrap_socket(s, ca_certs="server.crt", cert_reqs=ssl.CERT_REQUIRED)
 ssl_sock.connect(('localhost',8080))

 #Payload Send
 ssl_sock.sendall(payload)
 data = ssl_sock.recv(1024)
 print("sending complete")

 #Decode and save in a JSON file
 payloadJSON = json.loads(payload.decode('utf-8'))
 with open('payload.json', 'w') as outFile:
        jsonApp = outFile.write(json.dumps(payloadJSON))


except Exception as e:
 print(e)
 print(ssl_sock.cipher())
 ssl_sock.close()


