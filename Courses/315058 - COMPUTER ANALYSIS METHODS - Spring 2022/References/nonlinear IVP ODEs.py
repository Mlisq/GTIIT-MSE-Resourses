import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize as op
import scipy.integrate as ite

def fun1(t,y):
    return -0.5*y
sol=ite.solve_ivp(fun1,[0,20],[4])  #起始值0终值20 y(0)=4 后面还有个t_eval [0,20,1000] 1000为数据点的数（自定义）
print(sol.t)