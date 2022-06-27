import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize as op
import scipy.integrate as ite

#Bisection
def func(x):
    return x**2-1
print(op.bisect(func, 0, 2))    #0-2区间

#Newton-Raphson
def f0(x):
    return x**3-1

def f1(x):                      #f0的导数
    return 3*x**2
print(op.newton(f0, 1.5,f1))    #估计0点在x=1.5处