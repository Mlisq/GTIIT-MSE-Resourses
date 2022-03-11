# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 14:22:56 2020

@author: bai06125
"""
import numpy as np
import random

def numberList(numberIndex = 0, data = []):
    ranNum = random.randint(0,len(data)-1-numberIndex)
    data2 = []
    
    for i in range(numberIndex):
        data2.append(data[ranNum+i])
        
    numberList = []
    _SDEV = np.std(data2)
    _AVE = np.average(data2)
    _SDER = _SDEV/(np.sqrt(len(data2)))
    numberList.append([_SDEV,_AVE,_SDER])
    
    return numberList


data = np.load('data2.npy')

List = numberList(150,data)
print(List)




