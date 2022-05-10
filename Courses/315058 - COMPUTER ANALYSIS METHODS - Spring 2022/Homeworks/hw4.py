'''Homework 4
Q.1
Examine the convergence of the central difference method for approximating
derivatives with data spacing dx in the range of [0.001:0.6]. Plot 3 error curves
(error as a function of dx) for trial function sin(x) at x=0, 0.5, 1.0 in log scale, and
explain your results. Note: you should put your name in the title of the plot.
Q.2
Evaluate the integral of f(x) =
1
1+𝑥
2
over the range of [−10: 10] using 4, 6, 8, 10
points Newton-Cotes method, and compare the error from these methods with
the error from 4-point Gaussian quadrature.
NOTE: Explain and summarize your results in a small paragraph.
Q.3
Calculate the volume of a general ellipsoid with a=3, b=4, c=5 using
1. multivariable quadrature
2. Simpson’s method
Find the dx (assuming the same spacing along x and y axis) in the Simpson method
which gives similar error as the multivariable quadrature. Compare the results with
the analytical solution.
NOTE: summarize your results in a small paragraph. 
'''
import numpy as np 
import scipy.misc as mi
import scipy.integrate as ite 
import matplotlib.pyplot as plt


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


#Q3 参考 Xuanhao LIN 大哥来写的 我实在不知道simpson怎么写^^
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