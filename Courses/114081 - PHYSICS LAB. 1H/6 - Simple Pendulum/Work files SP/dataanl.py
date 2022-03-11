import numpy as np
import matplotlib.pyplot as plt

D1 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-17.8.npy'))
D2 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-19.4.npy'))
D3 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-20.4.npy'))
D4 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-21.7.npy'))
D5 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-23.3.npy'))
D6 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6.npy'))
D7 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-25.7.npy'))
D8 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-28.4.npy'))

ypoints = [D1,D2,D3,D4,D5,D6,D7,D8]
xpoints = np.sqrt([17.8,19.4,20.4,21.7,23.3,24.6,25.7,28.4])

f = np.average(2*np.pi*np.sqrt(xpoints**2/9.79127))
print(f)

def func(x,k,b):
    return k*x+b

from scipy.optimize import curve_fit

popt,_ = curve_fit(func,xpoints,ypoints)

lypoints = [func(xpoints[i],*popt) for i in range(len(xpoints))]

plt.xlabel('L^(1/2) [m^(1/2)]')
plt.ylabel('T[s]')

plt.figure(1)
plt.plot(xpoints,lypoints,'r',label = "FC Y={0}X+{1}".format(popt[0],popt[1]))
plt.plot(xpoints,ypoints,'.',label = 'Experimental Data')
plt.legend()

plt.show()


sumsquare = 0

diffs = ypoints - func(xpoints,*popt)
for i in range(len(diffs)):
    sumsquare += diffs[i]**2

SSE = sumsquare
sumsquare = 0

_diffs = np.average(ypoints)-func(xpoints,*popt)
for i in range(len(_diffs)):
    sumsquare += _diffs[i]**2
SST = sumsquare

R = 1 - SSE/SST

print(R)