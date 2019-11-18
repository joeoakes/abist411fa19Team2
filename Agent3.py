import pysftp, sys, smtplib, hashlib, Pyro4, json, zlib, datetime
from email.mime.text import MIMEText
from pymongo import MongoClient

#Connection permit
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts, 'host':'oz-ist-linux-oakes', 'username':'ftpuser', 'password':'test1234', 'port': 100}

try:

        #Connect to sftpuser and ge the json file
        with pysftp.Connection(**cinfo) as sftp:
                print("Connection made")
                try:
                        print("getting payload.json file")
                        sftp.get('/home/ftpuser/payloadReceive.json')
                except:
                        print("Log exception :", sys.exc_info()[0])

        #Open the file, read it and save it in data
        #print out data
        print("read the json file code from Agent2")
        payload = open('payloadReceive.json','rb')
        data = payload.read()
        payload.close()
        print(data)

        #verify the hash
        checksum = hashlib.sha256(data).hexdigest()
        print("sha256: ", checksum)

        #set up the email address and subject
        print("Emailing")
        fromAddress = 'dck5200@psu.edu'
        toAddress = 'dck5200@psu.edu'
        subject = 'Payload send'

        #open the json file and save it to msg
        with open('payloadReceive.json') as fp:
                msg = MIMEText(fp.read())

        #set msg's address abd subject
        msg['Subject'] = subject
        msg['From'] = fromAddress
        msg['To'] = toAddress

        #send the msg though ssl to the address
        s = smtplib.SMTP_SSL('authsmtp.psu.edu', 465)
        s.sendmail(fromAddress, [toAddress], msg.as_string())
        s.quit()

        client = MongoClient('localhost',27017)
        db = client.Team2
        collection = db.agent3
        print("Saved workflow action")
        post_id = collection.insert({"action": "Sent JSON Pyro4", "time" : datetime.datetime.now()})

except:
        print("Log exception 2: ", sys.exc_info()[0])


#Open the json file and save the contents to data
with open ('payloadReceive.json') as json_data:
        dataCompress = json_data.read()


# create a class of payload data
@Pyro4.expose
class PayloadData(object):
        def get_payload(self):
                data = dataCompress
                return "Here is your paylaod:\n"\
                        "{0}.".format(data)
# Compression
data_bytes = bytes(dataCompress, 'UTF-8')
payloadComp = zlib.compress(data_bytes)
print("Compressing the json object:", payloadComp)

print("Creating uri")
#create a pyro daemon
daemon = Pyro4.Daemon()
#register the payloadData as a pyro object
uri = daemon.register(PayloadData)

#creating the uri
print("Object uri=", uri)
daemon.requestLoop()



