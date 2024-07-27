import numpy as np
import matplotlib.pyplot as plt
N = 1
x = np.arange(-10, 10, N)
y = np.arange(-10, 10, N)
#Rectangular grid with points
X, Y = np.meshgrid(x, y)

#derivative
dy = X**2 - Y #Use uppercase
dx = np.ones(dy.shape)

norm = np.sqrt(dx**2 + dy**2)
dyu = dy/norm
dxu = dx/norm

#plot
plt.quiver(X, Y, dxu, dyu, color = "purple")
plt.title("Direction field for the differential equation")
plt.show()
