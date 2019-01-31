#!/usr/bin/python3

from tm1637 import TM1637
import time
import math
import csv
import random

log = open("logfile.csv", "a")
csvfile = csv.writer(log, delimiter = ",")
lcd1 = TM1637(4, 17)
lcd1.brightness(7)
start_time = time.time()
#csvfile.writerow(["probe1", "probe2", "time"])

def make_some_data(elapsed_time):
    csvfile.writerow([random.randint(100, 300), elapsed_time])
    log.flush()

def show_timer(lcd1):
    elapsed_time = math.floor(time.time() - start_time)
    lcd1.numbers(math.floor(elapsed_time / 3600), math.floor(elapsed_time % 3600 / 60), True)
    time.sleep(1)
    lcd1.numbers(math.floor(elapsed_time / 3600), math.floor(elapsed_time % 3600 / 60), False)
    time.sleep(1)
    make_some_data(elapsed_time)

# Main Loop
while True:
    show_timer(lcd1)
