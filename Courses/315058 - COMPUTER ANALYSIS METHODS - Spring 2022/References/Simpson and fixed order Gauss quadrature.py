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
N = 1717
x = np.linspace(-a, a, N+1)
def f3(x):
    return b*np.sqrt(1-((x**2)/a**2))
ylist = np.zeros(N+1)
for i in range(len(x)):
    y = np.linspace(-f3(x[i]), f3(x[i]), int(2 * f3(x[i]) / (2*a/N))+1)
    z = 2*c*np.sqrt(abs(1-((x[i]**2)/a**2) - ((y**2)/b**2)))
    ylist[i] = ite.simpson(z,y)
ss = ite.simpson(ylist,x)
ss_error = abs(ss - volume)
print("Result from simpson :",ss)
print("Error is ", ss_error)
print("Spacing is ", 2*a/N)