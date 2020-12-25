import numpy as np
import matplotlib.pyplot as plt
#define deltaT = 0.008

data = np.load('./data.npy')
t = data[0:,0]
x = data[0:,1]

plt.figure("Left side")
x1 = x[t < 3.5]
t1 = t[t < 3.5]

v = [None for _ in range(len(t1))]

for i in range(len(t1)-1):
    v[i] = (x1[i+1]-x1[i])/0.008

a = [None for _ in range(len(t1))]

for i in range(len(t1)-2):
    a[i] = (v[i+1]-v[i])/0.008

avg = np.average(np.abs(a[:-2]))
print("The acceleration of left side is %d"%avg)

plt.scatter(t1,a,s=10,c='#ff1212',marker='.')
plt.show()
    
plt.figure("Right side")
x2 = x[t > 3.5]
t2 = t[t > 3.5]

v = [None for _ in range(len(t2))]

for i in range(len(t2)-1):
    v[i] = (x2[i+1]-x2[i])/0.008

a = [None for _ in range(len(t2))]

for i in range(len(t2)-2):
    a[i] = (v[i+1]-v[i])/0.008

avg = np.average(np.abs(a[:-2]))
print("The acceleration of right side is %d"%avg)

plt.scatter(t2,a,s=10,c='#ff1212',marker='.')
plt.show()