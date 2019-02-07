import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3
import csv
import datetime

probe1 = [123, 128, 192, 178, 210, 223, 252, 268]
probe2 = [121, 135, 164, 212, 245, 298, 301, 303]
secs = [1549565281, 1549565282, 1549565283, 1549565284, 1549565285, 1549565286, 1549565287, 1549565288]

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

formatter = plt.FuncFormatter(hms2)

fig, ax = plt.subplots(figsize=(12, 7))
plt.plot(secs, probe1, label='Probe 1')
plt.plot(secs, probe2, label='Probe 2')
ax.xaxis.set_major_formatter(formatter)

plt.text(secs[-1]+1, probe1[-1]+1, probe1[-1], fontsize=15)
plt.text(secs[-1]+1, probe2[-1]+1, probe2[-1], fontsize=15)


plt.xlabel('Time (sec)')
plt.ylabel('Temp (F)')
plt.title('Temp History')
plt.legend(loc=2)

mpld3.save_html(fig, "test_example2.html")
