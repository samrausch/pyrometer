import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3
import matplotlib.dates as mdates
import csv
import datetime

probe1 = []
probe2 = []
pyro_time = []

def hms(x, pos=None):
	td = datetime.timedelta(seconds = x)
	hours = int((td.days * 24))
	hoursPlus = int(td.seconds / 3600)
	hours = hours + hoursPlus
	minutes = int(((td.seconds - (hoursPlus * 3600)) / 60))
	seconds = int(td.seconds - (minutes * 60) - (hoursPlus * 3600))
	tickString = str(hours) + ":" + str(minutes) + ":" + str(seconds)
	print(tickString)
	return tickString

with open('logfile.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        probe1.append(int(row[0]))
        probe2.append(int(row[1]))
        pyro_time.append(int(row[2]))

print("Data Imported")
mins = mdates.epoch2num(pyro_time)
secs = pyro_time
locator = mdates.AutoDateLocator()
formatter = mdates.AutoDateFormatter(locator)

print(secs)
print(mins)

fig, ax = plt.subplots(figsize=(12, 7))
plt.plot(mins, probe1, label='Probe 1')
plt.plot(mins, probe2, label='Probe 2')
ax.xaxis.set_major_formatter(formatter)
#ax.xaxis.set_major_formatter(plt.NullFormatter())

#plt.text(secs[-1]+1, probe1[-1]+1, probe1[-1], fontsize=15)
#plt.text(secs[-1]+1, probe2[-1]+1, probe2[-1], fontsize=15)


#plt.xlabel('Time (sec)')
#plt.ylabel('Temp (F)')
#plt.title('Temp History')
#plt.legend(loc=2)
#ax.set_xlim(left=int(secs[-1] - 7200))

mpld3.save_html(fig, "test_example2.html")
