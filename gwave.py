from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

#make a 3d graph to plot data
spacetime = plt.figure().add_subplot(projection="3d")

#get 3d test data
X, Y, Z = axes3d.get_test_data(0.05)
print(X)
print("")
print(Y)
print("")
print(Z)

#plot 3d data
spacetime.plot_surface(X, Y, Z, edgecolor="royalblue", lw=0.5, rstride=8, cstride=8, alpha=0.3)

#show the data on the graph
plt.show()
