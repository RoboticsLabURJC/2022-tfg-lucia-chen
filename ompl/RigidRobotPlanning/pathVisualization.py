from mpl_toolkits.mplot3d import Axes3D
import numpy
import matplotlib.pyplot as plt


fig = plt.figure()
# ax = fig.gca(projection='3d')
# ax.plot(data[:,0],data[:,1],data[:,2],'.-')
# ax.plot(data[:,0],data[:,1],'.-')
plt.subplot(1,2,1)
plt.title("App results")
data = numpy.loadtxt('app_path_rttstar.txt')
plt.plot(data[:,0],data[:,1],'.-')

plt.subplot(1,2,2)
plt.title("Code results")
data = numpy.loadtxt('code_path.txt')
plt.plot(data[:,0],data[:,1],'.-')

plt.show()
