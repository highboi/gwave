import numpy as np

def bivariate_distribution(domain, mean, variance):
	X = np.arange(-domain+mean, domain+mean, variance)
	Y = np.arange(-domain+mean, domain+mean, variance)
	X, Y = np.meshgrid(X, Y)
	R = np.sqrt(X**2+Y**2)
