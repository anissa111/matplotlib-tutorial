import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 2, 5, 1])

# Create figure and axes with subplots
fig, ax = plt.subplots(nrows=1, ncols=2)

# Plot on axes
ax[0].plot(x,y)
ax[1].plot(x,y, color='red', ls='--', marker='*', 
          markersize=25, markerfacecolor='k',
          mec='b')

plt.show()
#plt.savefig('basic.png')