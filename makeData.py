#!/usr/bin/python3

import time
import math
import csv
import random
import os

if os.path.exists("logfile.csv"):
    os.remove("logfile.csv")

log = open("logfile.csv", "a")
csvfile = csv.writer(log, delimiter = ",")
#csvfile.writerow(["probe1", "probe2", "time"])
start_time = time.time()
probe1 = []
probe2 = []
etime = []

probe1.append(350)
probe2.append(376)
etime.append(1)
i = 1563800000

while i < 1563864800:
	i = i + 30
	if probe1[-1] > 2500:
		probe1.append(probe1[-1] - random.randint(500, 800))
	else:
		probe1.append(probe1[-1] + random.randint(1, 8))
	if probe2[-1] > 2500:
		probe2.append(probe2[-1] - random.randint(700, 1000))
	else:
		probe2.append(probe2[-1] + random.randint(1, 8))
	etime.append(i)
	csvfile.writerow([probe1[-1], probe2[-1], math.floor(etime[-1])])
	log.flush()
#	time.sleep(1)
