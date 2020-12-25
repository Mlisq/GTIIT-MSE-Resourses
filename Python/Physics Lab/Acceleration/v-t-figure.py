import numpy as np
import matplotlib.pyplot as plt
#define deltaT = 0.008

data = np.load('./data.npy')

t = data[0:,0]
x = data[0:,1]
factor = 10

#Left side
plt.figure('Left side')
x1 = x[t < 3.5]
t1 = t[t < 3.5]
der1 = [None for _ in range(len(t1))]
for i in range(factor,len(t1)-factor,factor):
    der1[i] = (x1[i+1]-x1[i-1])/(0.008*factor)
plt.scatter(t1,der1,s=10,c='#ff1212',marker='.')
plt.show()

#Right side
plt.figure('Right side')
x2 = x[t > 3.5]
t2 = t[t > 3.5]
der2 = [None for _ in range(len(t2))]
for i in range(factor,len(t2)-factor,factor):
    der2[i] = (x2[i+factor]-x2[i-factor])/(0.008*factor)
plt.scatter(t2,der2,s=10,c='#ff1212',marker='.')
plt.show()
