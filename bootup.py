#!/usr/bin/python3

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
csvfile = csv.writer(log, delimiter = ",")

start_time = math.floor(time.time())

p1 = Process(target=get_ip)
p2 = Process(target=welcome)
p3 = Process(target=read_buttons)

mode = 1

lcd1 = TM1637(18, 17)
lcd2 = TM1637(4, 21)
lcd1.brightness(7)
lcd2.brightness(7)

sensor1 = MAX31855.MAX31855(25, 5, 6)
sensor2 = MAX31855.MAX31855(12, 13, 16)

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def read_buttons():
    global mode
    while True:
        input1 = GPIO.input(20)
        if input1 == False:
            mode = 2
            p1.terminate()
            p2.terminate()
        input2 = GPIO.input(19)
        if input2 == False:
            mode = 1
        input3 = GPIO.input(26)
        if input3 == False:
            bashCommand = "shutdown now"
            process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except:
        ip = '127.0.0.1'
        lcd1.scroll("No Connection")
    finally:
        s.close()
    ip_split = ip.split(".")
    lcd1.scroll("IP Address")
    for word in ip_split:
        lcd1.scroll(word)

def welcome():
    lcd2.scroll("Press top button to start")

def c_to_f(c):
    return c * 9.0 / 5.0 + 32.0

def get_temps(sensor1, sensor2):
    temp1 = sensor1.readTempC()
    internal1 = sensor1.readInternalC()
    temp2 = sensor2.readTempC()
    internal2 = sensor2.readInternalC()
    return c_to_f(temp1), c_to_f(internal1), c_to_f(temp2), c_to_f(internal2)
# temp1, internal1, temp2, internal2 = get_temps(sensor1, sensor2)

def hms(x):
    td = datetime.timedelta(seconds = x)
    hours = int((td.days * 24))
    hoursPlus = int(td.seconds / 3600)
    hours = hours + hoursPlus
    minutes = int(((td.seconds - (hoursPlus * 3600)) / 60))
    tickString = int(str(hours) + str(minutes))
    return tickString

while True:
    while mode == 1:
        p1.start()
        p2.start()
        p3.start()
#    p1.join()
#    p2.join()
#    p3.join()

    while mode == 2:
        temp1, internal1, temp2, internal2 = get_temps(sensor1, sensor2)
        elapsed_time = math.floor(time.time() - start_time)
        csvfile.writerow(temp1, temp2, elapsed_time)
        log.flush()
        lcd1.number(int(temp1))
        lcd2.number(int(temp2))
        time.sleep(5)
        display_time = hms(elapsed_time)
        lcd1.show("Time")
        lcd2.numbers(display_time, True)
        time.sleep(1)
        lcd2.numbers(display_time, False)
        time.sleep(1)
        lcd2.numbers(display_time, True)
        time.sleep(1)
        lcd2.numbers(display_time, False)
        time.sleep(1)
        lcd2.numbers(display_time, True)
        time.sleep(1)
