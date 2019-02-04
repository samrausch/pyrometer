#!/usr/bin/python3

import pandas as pd
import matplotlib.pyplot as plt, mpld3
#from matplotlib.pyplot import figure

data = pd.read_csv('logfile.csv', header=0)

print("Data imported")

topline = data['probe1']
bottomline = data['probe2']
elapsed_time = data['time']

print("Data defined")

#plt.figure(figsize=[10, 8])
#ax = fig.gca()
ax = plt.subplots()
l0 = ax.plot(topline, elapsed_time)
l1 = ax.plot(bottomline, elapsed_time)

#plt.plot(topline, elapsed_time)
#plt.plot(bottomline, elapsed_time)
#plt.legend(["United States", "China"], loc=0, fontsize=15)
#plt.ylabel("Cheeseburgers!", size=20)
#plt.xlabel("Beers!", size=20)
#plt.title("Drinks per Cheeseburger", size=30)
#plt.grid(True)

mpld3.save_html(fig, "test_example2.html")


