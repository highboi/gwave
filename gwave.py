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
size = 200

#a variable for the spacing the grids
spacing = 40

#a variable for spacing the grid lines on each grid
gridlinespacing = 5

#generate the 2d mesh for graphing repeatedly into layers
x, y = np.meshgrid(np.linspace(-size, size), np.linspace(-size, size))

#the values to manipulate using wave function to produce a 3d representation of any wave
r = np.sqrt(x**2+y**2)

#define values for the location(s) and weights of masses in spacetime (adding multiple masses to one array is useful)
masses = [[0, 100, 100, 1]]

'''
FUNCTIONS FOR MANIPULATING THE 2D GRIDS USING WAVE FUNCTIONS TO REPRESENT SPACETIME CURVATURE
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
	periodnum = phaseval / period

	#add exponents and a negative sign to make it into a curve
	periodnum = -(periodnum)**2

	#use eulers number to make the bell curve
	bellcurve = math.e**periodnum

	#add the amplitude necessary for this curve
	bellcurve = amplitude * bellcurve

	#return the resulting range of values
	return bellcurve

#a function for plotting a point mass
def plot_mass(x, y, z, mass):
	#plot the mass and make the size a multiple of the mass (mass is in kilograms)
	spacetime.scatter(x, y, z, c="magenta", s=mass*1000)

#plot all masses defined in the array of point masses
for mass in masses:
	plot_mass(mass[0], mass[1], mass[2], mass[3])

'''
FUNCTIONS FOR PLOTTING SPACETIME LAYERS IN 3 DIMENSIONS
'''
#function for layering grids along the z axis
def layer_z(warp=0):
	#graph layers along the z axis
	for elev in range(-size, size+spacing, spacing):
		#make an empty array with the same shape as the x or y coordinates
		z = np.empty(x.shape)
		z.fill(0)

		#add the elevation to the z coordinates
		z += elev

		#warp the fields according to the distance from each mass
		for mass in masses:
			#get the distance of this plane from the mass
			distance = z[0][0] - mass[0]

			#get the mass number
			weight = mass[3]*1000

			#if the plane is right on the mass, don't manipulate anything about it
			if not distance:
				continue

			#calculate the amplitude and the period of the gaussian distribution based on the mass and distance
			amplitude = -(weight / distance)
			period = (distance / weight)*1000

			#add a bell curve to this plane based on the distance from this mass
			z += bell_curve(x, period, amplitude, mass[0])
			z += bell_curve(y, period, amplitude, mass[1])

		#plot the 3d data
		spacetime.plot_wireframe(x, y, z, rstride=gridlinespacing, cstride=gridlinespacing, linewidth=0, color="red", alpha=0.5)

		#project contours onto the map for visualizing gravitational strain
		spacetime.contour(x, y, z, zdir="z", cmap="coolwarm", offset=-size)

#function for layering grids along the y axis
def layer_y(warp=0):
	#graph layers along the y axis
	for elev in range(-size, size+spacing, spacing):
		#make an empty array with the same shape as the x or y coordinates
		z = np.empty(x.shape)
		z.fill(0)

		#add the elevation to the z coordinates
		z += elev

		#warp the fields according to the distance from each mass
		for mass in masses:
			#get the distance of this plane from the mass
			distance = z[0][0] - mass[0]

			#get the mass number
			weight = mass[3]*1000

			#if the plane is right on the mass, don't manipulate anything about it
			if not distance:
				continue

			#calculate the amplitude and the period of the gaussian distribution based on the mass and distance
			amplitude = -(weight / distance)
			period = (distance / weight)*1000

			#add a bell curve to this plane based on the distance from this mass
			z += bell_curve(x, period, amplitude, mass[0])
			z += bell_curve(y, period, amplitude, mass[2])

		#plot the 3d data
		spacetime.plot_wireframe(x, z, y, rstride=gridlinespacing, cstride=gridlinespacing, linewidth=0, color="green", alpha=0.5)

		#project contours onto the map for visualizing gravitational strain
		spacetime.contour(x, z, y, zdir="y", cmap="coolwarm", offset=size)

#function for layering grids along the x axis
def layer_x(warp=0):
	#graph layers along the x axis
	for elev in range(-size, size+spacing, spacing):
		#make an empty array with the same shape as the x or y coordinates
		z = np.empty(x.shape)
		z.fill(0)

		#add the elevation to the z coordinates
		z += elev

		#warp the fields according to the distance from each mass
		for mass in masses:
			#get the distance of this plane from the mass
			distance = z[0][0] - mass[0]

			#get the mass number
			weight = mass[3]*1000

			#if the plane is right on the mass, don't manipulate anything about it
			if not distance:
				continue

			#calculate the amplitude and the period of the gaussian distribution based on the mass and distance
			amplitude = -(weight / distance)
			period = (distance / weight)*1000

			#add a bell curve to this plane based on the distance from this mass
			z += bell_curve(x, period, amplitude, mass[2])
			z += bell_curve(y, period, amplitude, mass[1])

		#plot the 3d data
		spacetime.plot_wireframe(z, y, x, rstride=gridlinespacing, cstride=gridlinespacing, linewidth=0, color="blue", alpha=0.5)

		#project contours onto the map for visualizing gravitational strain
		spacetime.contour(z, y, x, zdir="x", cmap="coolwarm", offset=size)

#create layers with different "warp" properties for each dimension
layer_x()
layer_y()
layer_z()

#show the data on the graph
plt.show()
