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
   print("receive payload ",message.payload)
   decrypted_message = cipher.decrypt(message.payload)   #decrypted_message = cipher.decrypt(encrypted_message)
   print("\nreceived message =",str(decrypted_message.decode("utf-8")))


client= paho.Client("client-pub")  #create client object client1.on_publish = on_publish                          #assign function to callback client1.connect(broker,port)                                 #establish connection client1.publish("house/bulb1","on")  
client.on_log=on_log
client.tls_set("/media/kannan/9A04D39F04D37CA7/Amrita/3rd year/6th semester/mqttPaper/mosquitto_Windows/ca.crt")
######
client.on_message=on_message
#####encryption
#cipher_key = Fernet.generate_key()
#cipher_key=b'WDrevvK8ZrPn8gmiNFjcOp2xovBr40TCwJlZOyI94IY='
#cipher = Fernet(cipher_key)
message = b'on33'
#message = b'the quick brown fox jumps over the lazy dog'
#encrypted_message = cipher.encrypt(message)
#out_message=encrypted_message.decode()# turn it into a string to send

##
print("connecting to broker ",broker)
client.connect(broker,port)#connect
print("publishing encrypted message ",message)
#out_message="on"
client.publish("house/bulb1",message)#publish
currentTime = datetime.datetime.now()
print("Timing: %s" %currentTime)
time.sleep(4)
client.disconnect() #disconnect
client.loop_stop() #stop loop
