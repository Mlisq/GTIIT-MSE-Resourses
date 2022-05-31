from scipy import integrate as ite
import numpy as np
import matplotlib.pyplot as plt



def func1(t,y,a,b):
    return [-2.0*a*b*y[0]-b*b*y[1]-np.sin(t),y[0]]

x1=np.linspace(0,np.pi*4,100)
sol1=ite.solve_ivp(func1,[0,np.pi*4.0],[0,0.01],t_eval=x1, args=(1.0,0.5))
plt.plot(sol1.t,sol1.y[1],label='l = 1,w0 = 0.5')

sol2=ite.solve_ivp(func1,[0,np.pi*4.0],[0,0.01],t_eval=x1, args=(1.0,1.0))
plt.plot(sol2.t,sol2.y[1],label='l = 1,w0 = 1.0')

sol3=ite.solve_ivp(func1,[0,np.pi*4.0],[0,0.01],t_eval=x1, args=(0.5,0.5))
plt.plot(sol3.t,sol3.y[1],label='l = 0.5,w0 = 0.5')

sol4=ite.solve_ivp(func1,[0,np.pi*4.0],[0,0.01],t_eval=x1, args=(0.5,1.0))
plt.plot(sol4.t,sol4.y[1],label='l = 0.5,w0 = 1.0')


plt.legend()
plt.show()

def func3(x, y, k):
    return [y[1], -k**2*y[0]]

def bc(ya, yb, k):
    return [ya[0], yb[0], ya[1]-k]

x = np.linspace(0, 1, 100)
y = np.zeros((2, 100))
y[0] = np.sin(x)
y[0, 1] = np.sin(x[1])
f = ite.solve_bvp(func3, bc, x, y, [10])
plt.plot(f.x, f.y[0])
s = ite.solve_bvp(func3, bc, x, y, [20])
plt.plot(s.x, s.y[0])
t = ite.solve_bvp(func3, bc, x, y, [30])
plt.plot(t.x, t.y[0])
fo = ite.solve_bvp(func3, bc, x, y, [40])
plt.plot(fo.x, fo.y[0])
fi = ite.solve_bvp(func3, bc, x, y, [50])
plt.plot(fi.x, fi.y[0])
plt.legend(["mode 1", "mode 2", "mode 3", "mode 4", "mode 5"])
plt.title("999006125 YangBai")
plt.show()