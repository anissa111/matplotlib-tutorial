import matplotlib.pyplot as plt
import numpy as np
import pickle

# open the binary file
infile = open('soi.pkl', 'rb')

# the three variables are stored in a single array, 
# can be unpacked in the load call directly
[date, soi, dsoi] = pickle.load(infile)

# close the file
infile.close()

# Make figure
plt.figure(figsize=(8,4))
ax = plt.gca()

# Add horizonal line
ax.axhline(y=0, color='grey', linewidth=0.75)

# Plot data
ax.plot(date, soi, color='black', linewidth=0.5)
ax.plot(date, dsoi, color='black')

# Fill above and below y=0
ax.fill_between(date, soi, where=soi > 0, color='red')
ax.fill_between(date, soi, where=soi < 0, color='blue')

# set axis range
ax.set_ylim([-3,3])

# label axes
plt.xlabel('Year')
plt.ylabel('SOI')
plt.title('Southern Oscillation Index', fontsize=15)

plt.show()
#plt.savefig('soi.png')