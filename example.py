from matplotlib.pyplot import figure,show
import numpy as np

x,y = np.meshgrid(np.linspace(0,2*np.pi), np.linspace(0,2*np.pi))

z = np.sin(x+0.5*y)
ax = figure().gca(projection='3d')
ax.plot_wireframe(x,y,z)
show()
