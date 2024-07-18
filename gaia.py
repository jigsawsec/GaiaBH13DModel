import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the grid for the 3D plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define the function for the black hole singularity
def black_hole_singularity(x, y):
    return -1 / np.sqrt(x**2 + y**2)

# Calculate the z values
z = black_hole_singularity(x, y)

# Plotting the 3D model
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='inferno')

# Adding labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Model of Black Hole Singularity (Gaia-BH1)')

plt.show()
