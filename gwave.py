'''
MODULES AND VARIABLES FOR PLOTTING
'''
from mpl_toolkits.mplot3d import axes3d
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import math

#a variable for the volume of the spacetime being simulated
size = 200

#make a 3d graph to plot data
fig = plt.figure()
spacetime = fig.add_subplot(projection="3d")

#setting labels for all axes
spacetime.set_xlabel("X")
spacetime.set_ylabel("Y")
spacetime.set_zlabel("z")

#setting the axes limits
spacetime.set_xlim([-size, size])
spacetime.set_ylim([-size, size])
spacetime.set_zlim([-size, size])

#a variable for the spacing the grids
spacing = 50

#a variable for spacing the grid lines on each grid
gridlinespacing = 5

#generate the 2d mesh for graphing repeatedly into layers
x, y = np.meshgrid(np.linspace(-size, size), np.linspace(-size, size))

#the values to manipulate using wave function to produce a 3d representation of any wave
r = np.sqrt((x+100)**2+(y+100)**2)

#define values for the location(s) and weights of masses in spacetime (adding multiple masses to one array is useful)
masses = [[0, 0, 0, 3], [-100, -100, -100, 5], [100, 100, 100, 1]]

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

#a function for plotting the masses in the mass array
def plot_masses():
	#plot all masses defined in the array of point masses
	for mass in masses:
		plot_mass(mass[0], mass[1], mass[2], mass[3])

'''
FUNCTIONS FOR PLOTTING SPACETIME LAYERS IN 3 DIMENSIONS
'''
#function for layering grids along the z axis
def layer_z(reduction=0):
	global spacetime

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
			distance = z[0][0] - mass[2]

			#get the mass number
			weight = mass[3]*1000

			#if the plane is right on the mass, don't manipulate anything about it
			if distance == 0:
				continue

			#calculate the amplitude and the period of the gaussian distribution based on the mass and distance
			amplitude = -(weight / distance)
			period = (distance / weight)*1000

			#reduce the values for this distortion if necessary
			amplitude -= reduction
			period -= reduction

			#create the input values for making the 3d bell curve with the mass location offsets taken into account
			r = np.sqrt((x-mass[0])**2 + (y-mass[1])**2)

			#the distortion for the peak/3d bell curve
			square_distortion = bell_curve(r, period, amplitude)
			#square_distortion = bell_curve(r, weight/20, amplitude)

			#add this distortion to this plane of the distortion
			z += square_distortion

		#plot the distortion created by this mass and orient it towards the location of the mass
		#spacetime.plot_wireframe(x, y, z, rstride=gridlinespacing, cstride=gridlinespacing, linewidth=1, color="red", alpha=0.5)

		#plot the contour created by this mass and orient it towards the location of the mass
		spacetime.contourf(x, y, z, cmap="seismic", zdir="z", offset=-size)

#function for layering grids along the y axis
def layer_y(reduction=0):
	global spacetime

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
			distance = z[0][0] - mass[1]

			#get the mass number
			weight = mass[3]*1000

			#if the plane is right on the mass, don't manipulate anything about it
			if distance == 0:
				continue

			#calculate the amplitude and the period of the gaussian distribution based on the mass and distance
			amplitude = -(weight / distance)
			period = (distance / weight)*1000

			#reduce the values for this distortion if necessary
			amplitude -= reduction
			period -= reduction

			#create the input values for making the 3d bell curve with the mass location offsets taken into account
			r = np.sqrt((x-mass[0])**2 + (y-mass[2])**2)

			#the distortion for the peak/3d bell curve
			square_distortion = bell_curve(r, period, amplitude)
			#square_distortion = bell_curve(r, weight/20, amplitude)

			#add this distortion to this plane of the distortion
			z += square_distortion

		#plot the distortion created by this mass and orient it towards the location of the mass
		#spacetime.plot_wireframe(x, z, y, rstride=gridlinespacing, cstride=gridlinespacing, linewidth=1, color="red", alpha=0.5)

		#plot the contour created by this mass and orient it towards the location of the mass
		spacetime.contourf(x, z, y, cmap="seismic", zdir="y", offset=size)

#function for layering grids along the x axis
def layer_x(reduction=0):
	global spacetime

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
			if distance == 0:
				continue

			#calculate the amplitude and the period of the gaussian distribution based on the mass and distance
			amplitude = -(weight / distance)
			period = (distance / weight)*1000

			#reduce the values for this distortion if necessary
			amplitude -= reduction
			period -= reduction

			#create the input values for making the 3d bell curve with the mass location offsets taken into account
			r = np.sqrt((x-mass[2])**2 + (y-mass[1])**2)

			#the distortion for the peak/3d bell curve
			square_distortion = bell_curve(r, period, amplitude)
			#square_distortion = bell_curve(r, weight/20, amplitude)

			#add this distortion to this plane of the distortion
			z += square_distortion

		#plot the distortion created by this mass and orient it towards the location of the mass
		#spacetime.plot_wireframe(z, y, x, rstride=gridlinespacing, cstride=gridlinespacing, linewidth=1, color="red", alpha=0.5)

		#plot the contour created by this mass and orient it towards the location of the mass
		spacetime.contourf(z, y, x, cmap="seismic", zdir="x", offset=-size)

'''
#variable for storing frames of video
frames = 100

def update(num):

ani = animation.FuncAnimation(fig, update, frames, fargs=(), interval=frames, blit=False)

'''

#create layers with different "warp" properties for each dimension
'''
layer_z()
layer_y()
layer_x()
'''

#plot the masses
#plot_masses()

#show the data on the graph
#plt.show()

#generate frames and alter data each iteration
for i in range(100):
	#print the current frame number
	print("FRAME NUMBER:", i)

	#make a 3d graph to plot new
	fig = plt.figure()
	spacetime = fig.add_subplot(projection="3d")

	#setting labels for all axes
	spacetime.set_xlabel("X")
	spacetime.set_ylabel("Y")
	spacetime.set_zlabel("z")

	#setting the axes limits
	spacetime.set_xlim([-size, size])
	spacetime.set_ylim([-size, size])
	spacetime.set_zlim([-size, size])

	#manipulate the mass locations
	for mass in masses:
		mass[0] += 2

	print(masses)

	#layer the new distortions in the virtual spacetime
	layer_z()
	layer_y()
	layer_x()

	#save this plot as a png image
	plt.savefig("distortion{frame:02d}.png".format(frame=i))

	#close this figure and clear the plot for the next frame
	plt.close(fig)
	#plt.clf()
