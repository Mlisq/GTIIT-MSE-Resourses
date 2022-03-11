# -*- coding: utf-8 -*-
# Coding by Bai and Luo / 2020.11.25


import math
import numpy as np
import matplotlib.pyplot as plt

def RomanTest(_d):                 #To remove outlier
    _SDE = np.std(_d)
    _AVE = np.average(_d)

    n = len(_d)

    c = 0.9969+0.4040*(math.log(n))    #Found it on the web

    X_MAX = _AVE + c*_SDE
    X_MIN = _AVE - c*_SDE

    BADDATA = []
    GOODDATA = []
    
    for i in range(n):
        if X_MIN < _d[i] < X_MAX:
            GOODDATA.append(_d[i])
        else:
            #print(_d[i])
            BADDATA.append(_d[i])    
        
    if len(BADDATA) == 0:         
        return GOODDATA

    return RomanTest(GOODDATA)

def normalDist_x(u,sigma):
    return np.linspace(u - 3*sigma, u + 3*sigma, 50)

def normalDist_y(x,u,sigma):
    #fact=.3
    return np.exp(-(x - u) ** 2 / (2 * sigma ** 2)) / (np.sqrt(2 * np.pi) * sigma)

data2 = np.load('data2.npy')
_data = RomanTest(data2)
_SDE = np.std(_data)
_AVE = np.average(_data)

x = normalDist_x(_AVE,_SDE)
y = normalDist_y(x,_AVE,_SDE)
bins = 10

hist_fact = len(_data)*(6*_SDE)/bins

plt.title('Hist & ND Image')
plt.xlabel('Time(s)')
plt.ylabel('Numbers')
plt.plot(x , y*hist_fact , "r", linewidth = 2,label = 'Normal Distribution')
#plt.grid(True)
plt.hist(_data,bins,color = "skyblue",label = 'bins=%d'%bins)
plt.legend()
plt.savefig('NormalDistribution.png')
plt.show()
