#!/usr/bin/python3 -u

from multiprocessing import Process
from tm1637 import TM1637
import socket
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MAX31855.MAX31855 as MAX31855
import RPi.GPIO as GPIO
import subprocess
import math
import csv
import os
import datetime

if os.path.exists("logfile.csv"):
    os.remove("logfile.csv")

log = open("logfile.csv", "a")
csvfile = csv.writer(log, delimiter=",")

start_time = math.floor(time.time())

mode = 1

lcd1 = TM1637(5, 6)
lcd2 = TM1637(26, 21)
lcd1.brightness(2)
lcd2.brightness(2)

sensor1 = MAX31855.MAX31855(4, 17, 18)
sensor2 = MAX31855.MAX31855(27, 22, 23)

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def get_ip():
#    lcd1.scroll("Welcome")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
        lcd2.scroll("No Connection")
    finally:
        s.close()
        ip_split = ip.split(".")
    while True:
        lcd2.scroll("")
        lcd2.scroll("IP Address")
        for word in ip_split:
            lcd2.scroll(word)


def welcome():
    while True:
        lcd1.scroll("")
        lcd1.scroll("Press top button to start")


def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0


def get_temps(sensor1, sensor2):
    temp1 = sensor1.readTempC()
    internal1 = sensor1.readInternalC()
    temp2 = sensor2.readTempC()
    internal2 = sensor2.readInternalC()
    return c_to_f(temp1), c_to_f(internal1), c_to_f(temp2), c_to_f(internal2)
    # to call this function:
    # temp1, internal1, temp2, internal2 = get_temps(sensor1, sensor2)


def hms(x):
    td = datetime.timedelta(seconds=x)
    hours = int((td.days * 24))
    hoursPlus = int(td.seconds / 3600)
    hours = hours + hoursPlus
    minutes = int(((td.seconds - (hoursPlus * 3600)) / 60))
    tickString = int(str(hours) + str(minutes))
    return tickString


def pyrometer_main():
    while True:
        temp1, internal1, temp2, internal2 = get_temps(sensor1, sensor2)
        elapsed_time = math.floor(time.time() - start_time)
#        csvfile.writerow([int(temp1), int(temp2), int(time.time())])
        print(temp1)
        print(temp2)
#        print(int(temp1))
#        print(int(temp2))
        print(internal1)
        print(internal2)
        log.flush()
        lcd1.number(int(temp1))
        lcd2.number(int(temp2))
        time.sleep(4)
        lcd1.number(0)
        lcd2.number(0)
        time.sleep(1)


p1 = Process(target=get_ip)
p2 = Process(target=welcome)
p4 = Process(target=pyrometer_main)
p1.start()
p2.start()

while True:
    input1 = GPIO.input(12)
    if input1 == False:
        print("Starting pyrometer")
        if p1.is_alive():
            p1.terminate()
        if p2.is_alive():
            p2.terminate()
        lcd2.scroll("")
        lcd1.scroll("Starting")
#        p4.join(timeout=0)
        if p4.is_alive():
            print("Pyrometer already running")
        else:
            p4 = Process(target=pyrometer_main)
            p4.start()
    input2 = GPIO.input(13)
    if input2 == False:
        print("Stopping pyrometer")
        if p4.is_alive():
            p4.terminate()
        lcd2.scroll("")
        lcd1.scroll("Stopping")
#        p1.join(timeout=0)
        if p1.is_alive():
            print("Get IP already running")
        else:
            p1 = Process(target=get_ip)
            p1.start()
#        p2.join(timeout=0)
        if p2.is_alive():
            print("Welcome is already running")
        else:
            p2 = Process(target=welcome)
            p2.start()
    input3 = GPIO.input(16)
    if input3 == False:
        if p1.is_alive():
            p1.terminate()
        if p2.is_alive():
            p2.terminate()
        if p4.is_alive():
            p4.terminate()
        print("Shutting down")
        lcd2.scroll("")
        lcd1.scroll("Shutting down")
        bashCommand = "shutdown now"
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

