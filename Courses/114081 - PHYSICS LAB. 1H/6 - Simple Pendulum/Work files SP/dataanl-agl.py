
import numpy as np
import matplotlib.pyplot as plt

#factor = 2*np.pi*np.sqrt(0.246/9.79127)
#print(factor)
D1 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6.npy')) #/factor
D2 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-9.npy')) #/factor
D3 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-12.npy')) #/factor
D4 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-15.npy')) #/factor
D5 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-20.npy'))#/factor
D6 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-25.npy'))#/factor
D7 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-30.npy'))#/factor
D8 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-40.npy'))#/factor
D9 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-50.npy'))#/factor
D10 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-60.npy'))#/factor
D11 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-70.npy'))#/factor
D12 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-80.npy'))#/factor
D13 = np.average(np.load('/Users/baiyang/Desktop/Workspace/Physics Lab/Simple Pendulum/Datas/data-24.6-90.npy'))#/factor
ypoints = [D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13]
xpoints = [9,12,15,20,25,30,40,50,60,70,80,90]

def func(x,a,b):
    return a*x**2 + b


plt.figure(1)
plt.plot(xpoints,ypoints,'.',label = 'Experimental Data')

from scipy.optimize import curve_fit
popt,_ = curve_fit(func,xpoints,ypoints)

lypoints = [func(xpoints[i],*popt) for i in range(len(xpoints))]
plt.ylabel('T[s]')
plt.xlabel('Angle[Degree]')
plt.plot(xpoints,lypoints,'r',label = "FC Y={0}x^2+{1}".format(popt[0],popt[1]))

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



