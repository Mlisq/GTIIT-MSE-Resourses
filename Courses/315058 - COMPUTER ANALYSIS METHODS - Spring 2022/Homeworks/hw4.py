import numpy as np 
import scipy.misc as mi
import scipy.integrate as ite 
import matplotlib.pyplot as plt

#Q3
a, b, c = 3, 4, 5
def f1(y,x):
    return 2*c*np.sqrt(1 - ((x**2)/a**2) - ((y**2)/b**2))
def f2(x):
    return [(-1) * b * np.sqrt(1 - ((x**2)/a**2)), b * np.sqrt(1 - ((x**2)/a**2))]
nq = ite.nquad(f1, [f2, [-a , a]])
error = np.abs(nq[0] - (4/3)*np.pi*a*b*c)
print("Result from nqaud :",nq[0])
print("Error is ", error)
print("---------------------")


'''
#Q2
func = lambda x0: 1/(1+x0**2)
t = ite.fixed_quad(func, -10, 10, n=4)
print("4th order Gaussian : Result:", t[0],"Error :", abs(t[0] - 2*np.arctan(10)))
print("--------------")
for N in [4,6,8,10]:
    x=np.linspace(-10,10,N+1)
    weight,B=ite.newton_cotes(N,1)
    dx=20/N
    quad=dx*np.sum(weight*(1/(1+x**2)))
    error=abs(quad-2*np.arctan(10))
    print('{:2d} order Newton-Cotes: Result: {:10.9f} Error : {:.5e}'.format(N,quad,error))
'''

'''
#Q1
def f(x):
    return np.sin(x)

True_derivative = np.cos(0),np.cos(0.5),np.cos(1)

_dx = np.linspace(0.001, 0.6)

plt.title("Yang Bai 999006125")
plt.xlabel("Value of dx")
plt.ylabel("Error of Derivative")
plt.plot(_dx, True_derivative[0] - mi.derivative(f, 0, _dx), '.', color = '#FF5A40', label = 'x = 0')
plt.plot(_dx, True_derivative[1] - mi.derivative(f, 0.5, _dx), '.', color = '#60A9F7', label = 'x = 0.5')
plt.plot(_dx, True_derivative[2] - mi.derivative(f, 1, _dx), '.', color = '#4CE082', label = 'x = 1')
plt.legend()
plt.show()
'''