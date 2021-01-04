import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
def order(x,a,b,c):
    return a*x+b*x**2+c

data = np.load('./data.npy')

t = data[0:,0]
x = data[0:,1]
x = -x.astype(float)

#plt.figure(1)
#plt.plot(t,x,'r',label='original data')
#plt.legend()
#plt.show()

index = (np.where(x == np.max(x)))[0][0]

#Left Side
plt.figure('left side')
plt.xlabel('Time[s]')
plt.ylabel('Displacement[m]')
plt.plot(t[0:index],x[0:index],'g',label = 'Left side curve')
popt,_ = curve_fit(order,t[0:index],x[0:index])
plt.plot(t[0:index],order(t[0:index],*popt),'r',label = 'fitting curve')
print("The acceleration of right side should be : {} m/s^2".format(2*popt[1]))

print("Curve equation of left is {0}*t{1}*t**2{2}".format(popt[0],popt[1],popt[2]))

plt.legend()
plt.show()


#Right Side
plt.figure('Right side')
plt.xlabel('Time[s]')
plt.ylabel('Displacement[m]')
plt.plot(t[index:],x[index:],'b',label = 'Right side curve')
popt,_ = curve_fit(order,t[index:],x[index:])
plt.plot(t[index:],order(t[index:],*popt),'r',label = 'fitting curve')
print("The acceleration of left side should be : {} m/s^2".format(2*popt[1]))

print("Curve equation of right is {0}*t{1}*t**2{2}".format(popt[0],popt[1],popt[2]))

plt.legend()
plt.show()


