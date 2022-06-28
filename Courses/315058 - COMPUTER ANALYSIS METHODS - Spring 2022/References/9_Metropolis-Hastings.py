#  Implementation of the Metropolis-Hastings algorithm 
#  Lecture 11 MCMC
#  An alg. to reach a desired distribution by controlling transistions between states
#  similar to simulated annealing... more or less

import numpy as np
import matplotlib.pyplot as plt
rng = np.random.default_rng()

#constants
mcs = 100 #just copy from wn, 
          # don't know whether it stands for Markov chain size 
          # or mathematics with computer science ^^

xarray = np.arange(0,mcs,1)

#desire distribution
def desire_dist(x):
    return np.exp(-(x-0.5)*(x-0.5)/0.01)

#MH alg.
def mcmc(n):
    s1 = rng.random((n,1))
    for x in range(0,n-1):
        xp = rng.random()
        pa = desire_dist(xp)/desire_dist(s1[x])
        if pa >= 1:
            s1[x+1] = xp
        else:
            p1 = rng.random()
            if p1 > pa:
                s1[x+1] = s1[x]
            else:
                s1[x+1] = xp
    return s1

def barstat(a,begin,end):
    stat = np.zeros(10)
    for i in range(begin,end):
        for j in range(0,9):
            if a[i]>j*0.1 and a[i]<(j+1)*0.1:
                stat[j] += 1
    return stat

yarray = mcmc(mcs)
bar = barstat(yarray,10,90)

#plot
plt.plot(xarray,yarray)
plt.show()
plt.plot(bar)
plt.show()

