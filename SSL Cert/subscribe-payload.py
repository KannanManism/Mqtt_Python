import time
import datetime
import paho.mqtt.client as paho
#from cryptography.fernet import Fernet
broker="localhost"
port=8883
#broker="192.168.1.206"
#define callback
def on_log(client, userdata, level, buf):
    print("log: ",buf)
def on_message(client, userdata, message):
   #time.sleep(1)
   print("receive message= ",message.payload)
   currentTime = datetime.datetime.now()
   print("Timing: %s" %currentTime)
   
   #decrypted_message = cipher.decrypt(message.payload)   #decrypted_message = cipher.decrypt(encrypted_message)
   #print("\nreceived message =",str(decrypted_message.decode("utf-8")))
   #print("\nreceived message =",str(message))

client= paho.Client("client-001")  #create client object client1.on_publish = on_publish                          #assign function to callback client1.connect(broker,port)                                 #establish connection client1.publish("house/bulb1","on")  
client.on_log=on_log
client.tls_set("/media/kannan/9A04D39F04D37CA7/Amrita/3rd year/6th semester/mqttPaper/mosquitto_Windows/ca.crt")
######
client.on_message=on_message
#####encryption
#cipher_key =b'WDrevvK8ZrPn8gmiNFjcOp2xovBr40TCwJlZOyI94IY='
#cipher = Fernet(cipher_key)

print("connecting to broker ",broker)
client.connect(broker,port)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("house/bulb1")#subscribe
count=0
while count <60:
    time.sleep(1)
    count+=1

client.disconnect() #disconnect
client.loop_stop() #stop loop
