import time
import paho.mqtt.client as paho
import datetime
from cryptography.fernet import Fernet
broker="localhost"
#broker="192.168.1.206"
#define callback
def on_log(client, userdata, level, buf):
    print("log: ",buf)
def on_message(client, userdata, message):
   #time.sleep(1)
   print("receive payload ",message.payload)
   decrypted_message = cipher.decrypt(message.payload)   #decrypted_message = cipher.decrypt(encrypted_message)
   print("\nreceived message =",str(decrypted_message.decode("utf-8")))
   currentTime = datetime.datetime.now()
   print("Timing: %s" %currentTime)


client= paho.Client("client-001")  #create client object client1.on_publish = on_publish                          #assign function to callback client1.connect(broker,port)                                 #establish connection client1.publish("house/bulb1","on")  
client.on_log=on_log
######
client.on_message=on_message
#####encryption
cipher_key =b'WDrevvK8ZrPn8gmiNFjcOp2xovBr40TCwJlZOyI94IY='
cipher = Fernet(cipher_key)

print("connecting to broker ",broker)
client.connect(broker)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("house/bulb1")#subscribe
count=0
while count <60:
    time.sleep(1)
    count+=1

client.disconnect() #disconnect
client.loop_stop() #stop loop
