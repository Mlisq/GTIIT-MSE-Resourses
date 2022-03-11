import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

#define deltaT = 0.008
def order(x,k,b):
    return k*x+b

data = np.load('./data.npy')

t = data[0:,0]
x = data[0:,1]
x = -x.astype(float)
factor = 15

#Left side
plt.figure('Left side')
plt.xlabel("Time[s]")
plt.ylabel("Speed[m/s]")
x1 = x[t < 3.5]
t1 = t[t < 3.5]
x1 = x1[t1 > 1.7]
t1 = t1[t1 > 1.7]
der1 = [None for _ in range(len(t1))]
for i in range(factor,len(t1)-factor,factor):
    der1[i] = (x1[i+factor]-x1[i-factor])/(0.008*factor)
plt.scatter(t1,der1,s=10,c='#ff1212',marker='.',label = 'Experimental data--Left--Factor=15')

indexs = []
for i, ele in enumerate(der1):
    if ele != None:
        indexs.append(i)
t1 = t1[indexs]
der1 = [i for i in der1 if i != None]
popt,_ = curve_fit(order,t1,der1)
plt.plot(t1,order(t1,*popt),'g',label = 'Fitting curve')
print("The Acceleration for left is {} m/s^2".format(str(popt[0])))
_, _, r_value, _, _ = stats.linregress(t1, der1)
print("R-Square for left is {}".format(r_value**2))
print("Curve equation of left is {0}*t+{1}".format(popt[0],popt[1]))

plt.legend()
plt.show()

#Right side
plt.figure('Right side')
plt.xlabel("Time[s]")
plt.ylabel("Speed[m/s]")
x2 = x[t > 3.5]
t2 = t[t > 3.5]
der2 = [None for _ in range(len(t2))]
for i in range(factor,len(t2)-factor,factor):
    der2[i] = (x2[i+factor]-x2[i-factor])/(0.008*factor)
plt.scatter(t2,der2,s=10,c='#ff1212',marker='.',label='Experimental data--Right--Factor=15')

indexs = []
for i, ele in enumerate(der2):
    if ele != None:
        indexs.append(i)
t2 = t2[indexs]
der2 = [i for i in der2 if i != None]
popt,_ = curve_fit(order,t2,der2)
plt.plot(t2,order(t2,*popt),'g',label = 'Fitting curve')
print("The Acceleration for right is {} m/s^2".format(str(popt[0])))
_, _, r_value, _, _ = stats.linregress(t2, der2)
print("R-Square for right is {}".format(r_value**2))
print("Curve equation of right is {0}*t+{1}".format(popt[0],popt[1]))

plt.legend()
plt.show()
