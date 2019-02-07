import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt, mpld3
import csv
import datetime

probe1 = [123, 128, 192, 178, 210, 223, 252, 268]
probe2 = [121, 135, 164, 212, 245, 298, 301, 303]
secs = [1, 1800, 3600, 5400, 7200, 10800, 14403, 21645]

def hms(x, pos=None):
    td = datetime.timedelta(seconds = x)
    hours = int((td.days * 24))
    hoursPlus = int(td.seconds / 3600)
    hours = hours + hoursPlus
    minutes = int(((td.seconds - (hoursPlus * 3600)) / 60))
    seconds = int(td.seconds - (minutes * 60) - (hoursPlus * 3600))
    tickString = str(hours) + ":" + str(minutes) + ":" + str(seconds)
    print(td.seconds)
    print(tickString)
    print()
    return tickString

formatter = plt.FuncFormatter(hms)

fig, ax = plt.subplots(figsize=(12, 7))
plt.plot(secs, probe1, label='Probe 1')
plt.plot(secs, probe2, label='Probe 2')
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_ticks_position('bottom')
ax.tick_params(which='major', width=1.00, length=15)
ax.tick_params(which='minor', width=0.75, length=2.5, labelsize=10)
ax.xaxis.set_major_locator(plt.MultipleLocator(2000))
ax.xaxis.set_minor_locator(plt.MultipleLocator(250))

plt.text(secs[-1]+1, probe1[-1]+1, probe1[-1], fontsize=15)
plt.text(secs[-1]+1, probe2[-1]+1, probe2[-1], fontsize=15)


plt.xlabel('Time (sec)')
plt.ylabel('Temp (F)')
plt.title('Temp History')
plt.legend(loc=2)
#ax.set_xlim(left=int(secs[-1] - 18000))
plt.savefig("fig.png")

mpld3.save_html(fig, "test_example2.html")
