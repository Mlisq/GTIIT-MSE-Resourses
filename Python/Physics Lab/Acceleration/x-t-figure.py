import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def order(x,a,b,c):
    return a*x+b*x**2+c

data = np.load('./data.npy')

t = data[0:,0]
x = data[0:,1]

#plt.figure(1)
#plt.plot(t,x,'r',label='original data')
#plt.legend()
#plt.show()

index = (np.where(x == np.min(x)))[0][0]

plt.figure('left side')
plt.plot(t[0:index],x[0:index],'g',label = 'Left side curve')
popt,_ = curve_fit(order,t[0:index],x[0:index])
plt.plot(t[0:index],order(t[0:index],*popt),'r',label = 'fitting curve')
print(popt)
plt.legend()
print("The acceleration of right side should be : {} m/s^2".format(2*popt[1]))
plt.show()

plt.figure('Right side')
plt.plot(t[index:],x[index:],'b',label = 'Right side curve')
popt,_ = curve_fit(order,t[index:],x[index:])
plt.plot(t[index:],order(t[index:],*popt),'r',label = 'fitting curve')
print(popt)
plt.legend()
print("The acceleration of left side should be : {} m/s^2".format(2*popt[1]))
plt.show()


