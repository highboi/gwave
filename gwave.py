from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#make a 3d graph to plot data
spacetime = plt.figure().add_subplot(projection="3d")

#generate the 2d mesh for graphing repeatedly into layers
x, y = np.meshgrid(np.linspace(0, 100), np.linspace(0, 100))

#calculate the z-coordinates based on the x and y coordinates
z = x*y

#plot the 3d data
spacetime.plot_wireframe(x, y, z, rstride=20, cstride=20)

#show the data on the graph
plt.show()
