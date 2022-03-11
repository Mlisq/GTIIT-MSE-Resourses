# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 11:35:57 2020

@author: 86159
"""
import numpy as np
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
        print("No BADDATA")
        print()
        return GOODDATA
    else:
        print("BAD DATA EXIST:")
        print(BADDATA)
        print()
            
    return RomanTest(GOODDATA)


data = np.load('data.npy')

_data = RomanTest(data)


#L1遮光片长度 L2释放距离 t时间 θ角度

