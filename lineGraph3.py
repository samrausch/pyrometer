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
mins_intermediate = mdates.epoch2num(pyro_time)
mins = mdates.num2date(mins_intermediate)
secs = pyro_time

#print(secs)
#print(mins)
#print(mins_intermediate)
#print(pyro_time)

hourTicks = mdates.HourLocator()
tickFormat = mdates.DateFormatter('%H:%M')

fig, ax = plt.subplots(figsize=(12, 7))
ax.grid(True)
ax.xaxis.set_major_locator(hourTicks)
ax.xaxis.set_major_formatter(tickFormat)
plt.plot(mins, probe1, label='Probe 1')
plt.plot(mins, probe2, label='Probe 2')

plt.text(secs[-1]+1, probe1[-1]+1, probe1[-1], fontsize=15)
plt.text(secs[-1]+1, probe2[-1]+1, probe2[-1], fontsize=15)


#plt.xlabel('Time (sec)')
#plt.ylabel('Temp (F)')
#plt.title('Temp History')
#plt.legend(loc=2)
#ax.set_xlim(left=int(secs[-1] - 7200))

mpld3.save_html(fig, "/var/www/html/test_example2.html")
