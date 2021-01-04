import numpy as np
import matplotlib.pyplot as plt
#define deltaT = 0.008

data = np.load('./data.npy')
t = data[0:,0]
x = data[0:,1]
factor_V = 10
factor_A = 1

#Left Side
plt.figure("Left side")
plt.xlabel("Time[s]")
plt.ylabel("Acceleration[m/s^2]")
x1 = x[t < 3.5]
t1 = t[t < 3.5]
x1 = x1[t1 > 1.7]
t1 = t1[t1 > 1.7]
v1 = [None for _ in range(len(t1))]
for i in range(factor_V,len(t1)-factor_V,factor_V):
    v1[i] = (x1[i+factor_V]-x1[i-factor_V])/(0.008*factor_V)
v1 = [i for i in v1 if i != None]
a1 = [None for _ in range(len(v1))]
for i in range(factor_A, len(v1)-factor_A, factor_A):
    a1[i] = (v1[i + factor_A] - v1[i - factor_A])/(0.008*factor_A)
indexs = []
for i, ele in enumerate(a1):
    if ele != None:
        indexs.append(i)
t1 = t1[indexs]
a1 = [((-1)/10)*i for i in a1 if i != None]
plt.scatter(t1,a1,s=10,c='#ff1212',marker='.',label='Experimental data')
plt.legend()
plt.show()
print("The mean acceleration of left is {}m/s^2".format(np.average(a1)))

#Right Side
plt.figure("Right side")
plt.xlabel("Time[s]")
plt.ylabel("Acceleration[m/s^2]")
x2 = x[t > 3.5]
t2 = t[t > 3.5]
v2 = [None for _ in range(len(t2))]
for i in range(factor_V,len(t2)-factor_V,factor_V):
    v2[i] = (x2[i+factor_V]-x2[i-factor_V])/(0.008*factor_V)
v2 = [i for i in v2 if i != None]
a2 = [None for _ in range(len(v2))]
for i in range(factor_A, len(v2)-factor_A, factor_A):
    a2[i] = (v2[i + factor_A] - v2[i - factor_A])/(0.008*factor_A)

indexs = []
for i, ele in enumerate(a2):
    if ele != None:
        indexs.append(i)
t2 = t2[indexs]
a2 = [((-1)/10)*i for i in a2 if i != None]
plt.scatter(t2,a2,s=10,c='#ff1212',marker='.',label='Experimental data')
plt.legend()
plt.show()

print("The mean acceleration of right is {}m/s^2".format(np.average(a2)))


