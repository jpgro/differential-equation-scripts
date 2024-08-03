# imported libraries 
import numpy as np
import matplotlib.pyplot as plt

N = 1
#Set a grid with X and Y points
x = np.arange(-10, 10, N)
y = np.arange(-10, 10, N)
# Rectangular grid with points
X, Y = np.meshgrid(x, y)

# derivative
dy = (X*Y)/(Y**2 + 1)  # Use uppercase
dx = np.ones(dy.shape)

#Create a unit vector for each point in space
norm = np.sqrt(dx**2 + dy**2)
dyu = dy / norm
dxu = dx / norm

# plot the direction field
plt.quiver(X, Y, dxu, dyu, color="purple")
plt.title("Direction field for the differential equation")
plt.show()
