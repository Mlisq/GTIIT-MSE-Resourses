'''
9-16
Implementation of the Metropolis-Hastings algorithm             #9
Implementation of Monte-Carlo integration                       #10
Use bisection and Newton-Raphson for root finding               #11
Newton-Cotes integration                                        #12
Use Simpson and/or fixed order Gauss quadrature for integration #13
Solving simple/nonlinear IVP ODEs                               #14
Solving BVP ODEs with shooting method                           #15
Solving SDEs with Euler-Maruyama                                #16
'''

import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize as op
import scipy.integrate as ite
#9
#Codes from lecture

rng = np.random.default_rng()
def pf1(x):
    return np.exp(-(x-0.5)*(x-0.5)/0.01)
def mcmc(mcs):
    s1 = rng.random((                                                                                                                                           mcs,1))
    for x in range(0,mcs-1):
        xp = rng.random()
        pa = pf1(xp)/pf1(s1[x])
        if pa >= 1:
            s1[x+1] = s1[x]
        else:
            s1[x+1] = p

#10
#本质上就是求一个统计系概念的平均值
#Codes from lecture 求1/4半价为1的圆的面积

rng = np.random.default_rng()       
s2 = rng.random((100,2))            
hit = 0                             
total = 0
for s in s2:
    if s[0]*s[0]+s[1]*s[1] <= 1.0: 
        hit += 1
    total += 1

'''
hit/total = 半径为1的圆的1/4的面积 数据量越大这个值越精确
'''

#11
#二分法和牛顿法找根
#二分
def func(x):
    return x**2-1
print(op.bisect(func, 0, 2))

#牛顿
def f0(x):
    return x**3-1

def f1(x):                      #f0的导数
    return 3*x**2
print(op.newton(f0, 1.5,f1))

#12
#Newton-cotes 求出每一部分的权重再加在一起
#Example: 求0->pi sinxdx 的积分，精度分别为2，4，6，8
for N in [2,4,6,8]:
    x=np.linspace(0,np.pi,N+1)
    weight,B=integrate.newton_cotes(N,1)                #分N个part 求的每个part的权重和误差
    dx=np.pi/N
    quad=dx*np.sum(weight*np.sin(x))
    error=abs(quad-2.0)
    print('{:2d} {:10.9f} {:.5e}'.format(N,quad,error))

#13
#作业hw4

#14
def fun1(t,y):
    return -0.5*y
sol=ite.solve_ivp(fun1,[0,20],[4])  #起始值0终值20 y(0)=4 后面还有个t_eval [0,20,1000] 1000为数据点的数（自定义）
print(sol.t)

#15
#打靶法 我觉得就是迭代法 通过改变不同的初值找到满足ode条件的解
'''
lecture的例子没找到 我尝试写一下
给定一个ode函数 func 起始值0终值5 我们知道y(0)~1 y(5)~-1
'现在就只用带入不同的y(0)和y(5)(在1，-1附近的数)，求解这个ode，使其最终尽量收敛在x=5时收敛为-1，越接近-1，这个初值就越接近理想解
sol1=solve_ivp(func,[-5.0,5.0],[-0.0012*(1.0+a*0.2),1.0-(1.0+a*0.2)*0.000849],t_eval=ax)
sol1.y[1][49] --- 我们要的x=5时y的值
'''
