import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3
import matplotlib.axes as axes
#import matplotlib.dates as mdate
import matplotlib.ticker as mtick
import csv
import time

probe1 = []
probe2 = []
time = []

with open('logfile.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        probe1.append(int(row[0]))
        probe2.append(int(row[1]))
        time.append(int(row[2]))

print("Data Imported")
#secs = mdate.epoch2num(time)
secs = time
#print(secs)

#fig = plt.figure(figsize=[12, 7])
fig, ax = plt.subplots(figsize=(12, 7))
plt.plot(secs, probe1, label='Probe 1')
plt.plot(secs, probe2, label='Probe 2')

#plt.gcf().autofmt_xdate()
#plt.gca().xaxis.set_major_locator(mtick.FixedLocator(secs))
#plt.gca().xaxis.set_major_formatter(
#    mtick.FuncFormatter(lambda pos,_: time.strftime("%d-%m-%Y %H:%M:%S", time.localtime(pos)))
#    )

#print("\n")
#print(probe1[-1])
#print("\n")
#print(secs[-1])

#plt.annotate("Peanuts", xy=(secs[-1], probe1[-1]), xycoords=('data', 'data'), xytext=(-145, 0), textcoords='offset pixels')
#plt.annotate("Peanuts", xy=(secs[-1], probe1[-1])
plt.text(secs[-1]+1, probe1[-1]+1, probe1[-1])
plt.text(secs[-1]+1, probe2[-1]+1, probe2[-1])

plt.xlabel('Time (sec)')
plt.ylabel('Temp (F)')
plt.title('Temp History')
plt.legend(loc=2)
#ax.set_xlim(left=int(secs[-1] - 1800))

#date_fmt = '%d-%m-%y %H:%M:%S'

# Use a DateFormatter to set the data to the correct format.
#date_formatter = mdate.DateFormatter(date_fmt)
#ax.xaxis.set_major_formatter(date_formatter)

# Sets the tick labels diagonal so they fit easier.
#fig.autofmt_xdate()

mpld3.save_html(fig, "/var/www/html/pyrometer/test_example2.html")
