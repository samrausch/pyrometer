#!/usr/bin/python3

from tm1637 import TM1637
import socket
import time

lcd1 = TM1637(4, 17)
lcd1.brightness(7)
#lcd1.scroll("My IP Address Is")

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
        lcd1.scroll("No Connection")
    finally:
        s.close()
    return IP

while True:
    address = str(get_ip())
    address_split = address.split(".")
    lcd1.scroll("IP Address")
    for word in address_split:
        lcd1.scroll(word)
