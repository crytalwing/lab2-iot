import sys
from Adafruit_IO import MQTTClient
import time
import random
from simple_ai import *

AIO_FEED_IDs = ["button1", "button2"]
AIO_USERNAME = "dlhcmut"
AIO_KEY = "aio_MwOT5231ZAYKxQ4XL7dXkZt9s4Nd"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id: " + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

counter_ai = 5
while True:
    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 5
        ai_result = image_detector()
        print("AI output: ", ai_result)
        client.publish("ai", ai_result)
    time.sleep(1)
    pass