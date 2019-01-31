import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import csv
import sys

x = []
y = []

with open('logfile.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(y,x, label='Probe 1')
plt.xlabel('Time (sec)')
plt.ylabel('Temp (F)')
plt.title('Temp History')
plt.legend()
plt.savefig(sys.stdout.buffer)
#plt.show()
