'''
MODULES AND VARIABLES FOR PLOTTING
'''
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
import math

#make a 3d graph to plot data
spacetime = plt.figure().add_subplot(projection="3d")

#a variable for the volume of the spacetime being simulated
size = 100

#a variable for the spacing between each point in the spacetime mesh
spacing = 10

#generate the 2d mesh for graphing repeatedly into layers
x, y = np.meshgrid(np.linspace(0, size), np.linspace(0, size))

'''
PLOTTING 2D LAYERS ON EACH AXIS FOR A 3D GRID MESH REPRESENTING SPACE-TIME
'''
#a function for generating a wave with certain properties
def wave(inputvals, period, amplitude, phaseshift=0):
	#make the fraction to multiply inside of the sine function for adjusting the period
	inputnum = 1 / (period/(2*np.pi))

	#make the base wave function with the period
	wavefunc = np.sin( (inputnum * inputvals) + phaseshift)

	#add the effect of the amplitude to the wave function
	wavefunc = amplitude*wavefunc

	#return the resulting range of values as a wave function
	return wavefunc

#a function for generating a bell curve
def bell_curve(inputvals, period, amplitude, phaseshift=0):
	#shift the input values according to the phase shift of the curve
	phaseval = (inputvals - phaseshift)

	#add the period to the math transformation (width of the curve)
	inputnum = phaseval / period

	#add exponents and a negative sign to make it into a curve
	inputnum = -(inputnum)**2

	#use eulers number to make the bell curve
	bellcurve = math.e**inputnum

	#add the amplitude necessary for this curve
	bellcurve = amplitude * bellcurve

	#return the resulting range of values
	return bellcurve

#function for layering grids along the z axis
def layer_z(warp=0):
	#graph layers along the z axis
	for elev in range(0, size+spacing, spacing):
		#make an empty array with the same shape as the x or y coordinates
		z = np.empty(x.shape)
		z.fill(0)

		#add the elevation to the z coordinates
		z += elev

		#warp the 2d grid using a wave function
		z += warp

		#plot the 3d data
		spacetime.plot_wireframe(x, y, z, rstride=spacing, cstride=spacing, linewidth=1, color="red", alpha=0.5)

#function for layering grids along the y axis
def layer_y(warp=0):
	#graph layers along the y axis
	for elev in range(0, size+spacing, spacing):
		#make an empty array with the same shape as the x or y coordinates
		z = np.empty(x.shape)
		z.fill(0)

		#add the elevation to the z coordinates
		z += elev

		#warp the 2d grid using a wave function
		z += warp

		#plot the 3d data
		spacetime.plot_wireframe(x, z, y, rstride=spacing, cstride=spacing, linewidth=1, color="green", alpha=0.5)

#function for layering grids along the x axis
def layer_x(warp=0):
	#graph layers along the x axis
	for elev in range(0, size+spacing, spacing):
		#make an empty array with the same shape as the x or y coordinates
		z = np.empty(x.shape)
		z.fill(0)

		#add the elevation to the z coordinates
		z += elev

		#warp the 2d grid using a wave function
		z += warp

		#plot the 3d data
		spacetime.plot_wireframe(z, y, x, rstride=spacing, cstride=spacing, linewidth=1, color="blue", alpha=0.5)

#create layers with different "warp" properties for each dimension
#layer_x(wave(x, 200, 5))
#layer_y(wave(x, 200, 10))
layer_z(bell_curve(x, 20, 10, 50))
#layer_z(wave(x, 200, 20, np.pi))

#plot an example point with mass in spacetime
spacetime.scatter(50, 50, 50, c="red", s=1000, alpha=1)

#show the data on the graph
plt.show()
