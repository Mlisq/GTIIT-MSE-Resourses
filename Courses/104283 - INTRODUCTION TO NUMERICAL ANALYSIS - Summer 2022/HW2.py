from HW2a import newton
from HW2b import mod_newton
import numpy as np

MAX_ITERATION_NUMBER = 100
#Can't not get answer from the second function if this number smaller than 50 ^^'

def f(x):
    return 1-4*x*np.cos(x)+2*x**2+np.cos(2*x)
    #return x**2+6*x**5+9*x**4-2*x**3-6*x**2+1
    #return np.sin(3*x)+3*np.exp(-2*x)*np.sin(x)-3*np.exp(-x)*np.sin(2*x)-np.exp(-3*x)
    #return np.exp(3*x)-27*x**6+27*x**4*np.exp(x)-9*(x**2)*np.exp(2*x)

def df(x):
    return 4*x-2*np.sin(2*x)-4*(-x*np.sin(x)+np.cos(x))
    #return 30*x**4+36*x**3-6*x**2-10*x
    #return 3*np.cos(3*x) + 3*np.exp(-x)*np.sin(2*x) - 6*np.exp(-x)*np.cos(2*x) - 6*np.exp(-2*x)*np.sin(x) + 3*np.exp(-2*x)*np.cos(x) + 3*np.exp(-3*x)
    #return -162*x**5 + 27*x**4*np.exp(x) + 108*x**3*np.exp(x) - 18*x**2*np.exp(2*x) - 18*x*np.exp(2*x) + 3*np.exp(3*x)

def ddf(x):
    return 4*x*np.cos(x) + 8*np.sin(x) - 4*np.cos(2*x) + 4
    #return 120*x**3 + 108*x**2 - 12*x - 10
    #return -9*np.sin(3*x) + 9*np.exp(-x)*np.sin(2*x) + 12*np.exp(-x)*np.cos(2*x) + 9*np.exp(-2*x)*np.sin(x) - 12*np.exp(-2*x)*np.cos(x) - 9*np.exp(-3*x)
    #return 27*x**4*np.exp(x) - 810*x**4 + 216*x**3*np.exp(x) - 36*x**2*np.exp(2*x) + 324*x**2*np.exp(x) - 72*x*np.exp(2*x) + 9*np.exp(3*x) - 18*np.exp(2*x)

if __name__ == '__main__':
    nsolution, nite_times = newton(0.5, f, df, 1e-5, MAX_ITERATION_NUMBER)
    mnsolution, mnite_times = mod_newton(0.5, f, df, ddf, 1e-5, MAX_ITERATION_NUMBER)
    print("---------------------------------------------------")
    print("| In this function, we obtain that:               |")
    print("| [1]: In accuarcy:                               |")
    if(np.abs(f(nsolution) - 0) < np.abs(f(mnsolution) - 0)):
        print("| Newton method is more accuracy.                 |")
    else:
        print("| Modified Newton method is more accuracy.        |")
    print("|---------------------------------------------------")
    print("| [2]:In iteration times:                         |")
    if(nite_times < mnite_times):
        print("| Newton method is Faster.                        |")
    elif(nite_times > mnite_times):
        print("| Modified Newton method is Faster.               |")
    else:
        print("| Both Methods is in eqaully speed                |")
    print("---------------------------------------------------")
    


