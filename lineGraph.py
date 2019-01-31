import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('logfile.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='time', ylabel='temp', title="Time and Temp")
ax.grid()

fig.savefig("/var/www/html/pyrometer/figure.png")
plt.show()
