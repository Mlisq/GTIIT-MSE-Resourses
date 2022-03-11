# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:22:56 2020

@author: bai06125
"""
import numpy as np
import random
import math
import matplotlib.pyplot as plt

def normalDist_x(u,sigma):
    return np.linspace(u - 3*sigma, u + 3*sigma, 50)

def normalDist_y(x,u,sigma):
    #fact=.3
    return np.exp(-(x - u) ** 2 / (2 * sigma ** 2)) / (np.sqrt(2 * np.pi) * sigma)



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
        return GOODDATA
            
    return RomanTest(GOODDATA)

def returnList(number = 0,data = []):
    data2 = []
    for i in range(number):
        rdNum = random.randint(0,len(data)-1)
        data2.append(data[rdNum])
    _SDEV = np.std(data2)
    _SDER = _SDEV/(np.sqrt(len(data2)))
    _AVE = np.average(data2)
    return _SDEV,_SDER,_AVE,data2

data2 = np.load('data2.npy')
data = RomanTest(data2)

SDEV,SDER,AVE,_data = returnList(20,data)

'''
L = 10
Thelta = 4
rad = 0.0698132
g = 9.79127
L1 = 0.18
L2 = 0.29

rL = 0.001
rg = 0.000005
rThelta = 0.005
rL1 = rL
rL2 = rL

Tg = 2*L*(-(1/((2*math.sin(rad)*L1*g)**(1/2)+(2*math.sin(rad)*L2*g)**(1/2))**2)*((1/(4*math.sin(rad)*L1*g)**(1/2))*(2*math.sin(rad)*L1)+(1/(4*math.sin(rad)*L2*g)**(1/2))*(2*math.sin(rad)*L2)))

TL1 =  2*L * (-(1/((2*math.sin(rad)*L1*g)**(1/2)+(2*math.sin(rad)*L2*g)**(1/2))**2) * ((2*math.sin(rad)*g)/((4*math.sin(rad)*L1*g)**(1/2)))) 
TL2 =  2*L * (-(1/((2*math.sin(rad)*L1*g)**(1/2)+(2*math.sin(rad)*L2*g)**(1/2))**2) * ((2*math.sin(rad)*g)/((4*math.sin(rad)*L2*g)**(1/2))))          
TL = 2 * ((2*math.sin(rad)*g*L1)**(1/2) + (2*math.sin(rad)*g*L2)**(1/2))**(-1)

rt = np.sqrt((Tg*rg)**2 + (TL1*rL1)**2 + (TL2*rL2)**2 + (TL*rL)**2)

print(rt)
'''

bins = 6

x = normalDist_x(AVE,SDEV)
y = normalDist_y(x,AVE,SDEV)

hist_fact = len(_data)*(6*SDEV)/bins

plt.title('Hist & ND Image-20')
plt.xlabel('Time(s)')
plt.ylabel('Numbers')
plt.plot(x , y*hist_fact , "r", linewidth = 2,label = 'Normal Distribution')
#plt.grid(True)
plt.hist(_data,bins,color = "skyblue",label = 'bins=%d'%bins)
plt.legend()
plt.savefig('NormalDistribution20.png')

#print("The Average of the 50 random data is {ave}\nThe SDEV of the 50 random data is {sdev}\nThe SDER of the 50 random data is{sder}".format(ave=AVE, sdev=SDEV,sder=SDER))






