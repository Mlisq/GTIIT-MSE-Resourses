import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize as op
import scipy.integrate as ite

#Fixed order gauss
#1/1+x**2 在-10到10上的积分
func = lambda x0: 1/(1+x0**2)
t = ite.fixed_quad(func, -10, 10, n=4)                                                  #4order
print("4th order Gaussian : Result:", t[0],"Error :", abs(t[0] - 2*np.arctan(10)))
print("--------------")

#Simpson
#求椭圆体积 双重积分
a, b, c = 3, 4, 5
volume = (4/3)*np.pi*a*b*c
def f1(y,x):
    return 2*c*np.sqrt(1 - ((x**2)/a**2) - ((y**2)/b**2))
def f2(x):
    return [(-1) * b * np.sqrt(1 - ((x**2)/a**2)), b * np.sqrt(1 - ((x**2)/a**2))]
nq = ite.nquad(f1, [f2, [-a , a]])
error = np.abs(nq[0] - volume)
print("Result from nqaud :",nq[0])
print("Error is ", error)
print("---------------------")