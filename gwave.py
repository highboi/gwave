from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

#make a 3d graph to plot data
spacetime = plt.figure().add_subplot(projection="3d")

#a variable for the volume of the spacetime being simulated
size = 100

#generate the 2d mesh for graphing repeatedly into layers
x, y = np.meshgrid(np.linspace(0, size), np.linspace(0, size))


#loop in order to graph multiple 2d layers into a 3d representation of space-time
for elev in range(0, size, 5):
	print(elev)

	#make an empty array with the same shape as the x or y coordinates
	z = np.empty(x.shape)
	z.fill(0)

	#add the elevation to the z coordinates
	z += elev

	#plot the 3d data
	spacetime.plot_wireframe(x, y, z, rstride=5, cstride=5)

#show the data on the graph
plt.show()
