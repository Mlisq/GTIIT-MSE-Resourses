import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize as op
import scipy.integrate as ite

#求sinx 在 (0,pi) 上的积分
#Newton-cotes 曲线积分分成一个一个矩形，矩形分的越多越精确
for N in [2,4,6,8]:
    x=np.linspace(0,np.pi,N+1)
    weight,B=ite.newton_cotes(N,1)                
    dx=np.pi/N
    quad=dx*np.sum(weight*np.sin(x))
    error=abs(quad-2.0)
    print('{:2d} {:10.9f} {:.5e}'.format(N,quad,error))