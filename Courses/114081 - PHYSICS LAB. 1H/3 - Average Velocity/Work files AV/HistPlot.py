# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 15:25:52 2020

@author: bai06125
"""
import numpy as np
import matplotlib.pyplot as plt
import math

def RomanTest(_d):
    _SDE = np.std(_d)
    _AVE = np.average(_d)

    n = len(_d)

    c = 0.9969+0.4040*(math.log(n))

    X_MAX = _AVE + c*_SDE
    X_MIN = _AVE - c*_SDE

    BADDATA = []
    GOODDATA = []
    
    for i in range(n):
        if X_MIN < _d[i] < X_MAX:
            GOODDATA.append(_d[i])
        else:
            BADDATA.append(_d[i])
        
    if len(BADDATA) == 0:
        #print("No BADDATA")
        print()
        return GOODDATA
    else:
        #print("BAD DATA EXIST:")
        print(BADDATA)
        print()
            
    return RomanTest(GOODDATA)

data = np.load('data2.npy')
data2 = RomanTest(data)

SDEV = np.std(data2)
SDER = SDEV/(np.sqrt(len(data2)))
AVE = np.average(data2)

print("The Average of the data is {ave}\nThe SDEV of the data is {sdev}\nThe SDER of the data is{sder}".format(ave=AVE, sdev=SDEV,sder=SDER))

bins = 10
plt.title('Histogram')
plt.xlabel('Time(s)')
plt.ylabel('Numbers')
plt.hist(data2,bins,color = "skyblue",label = 'bins=%d'%bins)
plt.savefig('Historm.png')


