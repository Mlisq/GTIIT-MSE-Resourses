import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize as op
import scipy.integrate as ite

'''
D(d^2u/dx^2)+u-u^3=0
y0 = du/dx                 --> y0` = -y1+y1^3
y1 = u                     --> y1` = y0
B.C: y1(-5)~1 y1(5)~-1
'''
def f(t,y):
    return [-y[1]+y[1]**3,y[0]]

axis = np.linspace(-5, 5,50)

for spacing in range(1,6):
    icl = -0.0012*(1.0+spacing*0.2)
    icr = 1.0-(1.0+spacing*0.2)*0.000849
    sol = ite.solve_ivp(f, [-5,5], [icl,icr],t_eval=axis)
    if abs(sol.y[1][49] - (-1)) <= 0.01:
        print("A good potential solution with y1`: ",end='')
        print(icl,end='|||')
        print(" y0`: ",end='')
        print(icr,end='|||')
        print("y1(5) = ",end='')
        print(sol.y[1][49])
    else:
        print(sol.y[1][49])