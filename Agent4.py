\

import Pyro4, json, zlib, pika


try:
    uri = input("What is the Pyro uri of the greeting object? ").strip()
    PayloadData = Pyro4.Proxy(uri)
    print(PayloadData.get_payload())

    #payloadDecomp = zlib.decompress(payloadComp)
    
    
    
    print("Connecting to App 1")
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    print("App 1 Connected")
    channel.queue_declare(queue = 'hello')
    channel.basic_publish(exchange = '', routing_key = 'hello', body = 'Hello app 1')
    print(" [x] Sent 'Hello App 1'")
    
except Exception as e:
    print(e)


