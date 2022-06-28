#16. solving SDEs with Euler-Maruyama
# Import packages
import numpy as np
import matplotlib.pyplot as plt

#constant definition
T = 10
N = 10000
dT = T/N
T0 = 0
tarray = np.arange(T0,T,dT)
mu = 1
sigma = 1

#parameter definition
def dW(dT):
    return np.random.normal(0,np.sqrt(dT))

yarray = np.zeros(N)
yarray[0] = 1   #initial condition

#iteration
def EM():
    for i in tarray:
        t = T0 + (i-1)*dT
        y = yarray[i-1]
        yarray[i] = y + (mu - y)* dT + sigma * dW(dT)
        return yarray

# Plot
plt.plot(tarray, yarray)
plt.xlabel("time")
plt.ylabel("y")    
plt.show()