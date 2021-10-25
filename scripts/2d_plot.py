import matplotlib.pyplot as plt
import numpy as np

# Make a space to plot over
x = np.arange(-3.0, 3.0, 0.05)
y = np.arange(-3.0, 3.0, 0.05)

# define a meshgrid
X, Y = np.meshgrid(x, y)

# compute some function over this grid
Z = np.cos(X) + np.sin(Y)

# Make a 1x3 subplots
fig, ax = plt.subplots(nrows=1, ncols=3)

# Plot the imshow we made above on the first plot
ax[0].imshow(Z, interpolation='none', cmap='coolwarm', extent=[-3,3,-3,3], origin='lower')
ax[0].set_title('imshow')

# Plot the same data with contour
ax[1].contour(Z, cmap='coolwarm', extent=[-3,3,-3,3])
ax[1].set_title('contour')
ax[1].set_aspect('equal')

# Plot the same data again with contourf
ax[2].contourf(Z, cmap='coolwarm', extent=[-3,3,-3,3])
ax[2].set_title('contourf')
ax[2].set_aspect('equal')

plt.show()