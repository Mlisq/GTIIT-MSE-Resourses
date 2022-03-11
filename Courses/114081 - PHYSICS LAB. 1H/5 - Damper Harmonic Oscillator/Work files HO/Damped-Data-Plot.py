'''

For short spring: 
    k1 * x1 + 0.0708[kg] * 9.79127[N/Kg] = mg
    k1 * x2 + 0.1398[Kg] * 9.79127[N/Kg] = mg
    
    x2 - x1 = 10.1[cm] = 0.101[m]
    
    --> k1 = 6.68908545[N/m]
    
Same for long spring:   
    k2 * x1 + 0.0749[kg] * 9.79127[N/Kg] = mg
    k2 * x2 + 0.1426[Kg] * 9.79127[N/Kg] = mg
    
    --> k2 = 6.5630592[N/m]
    
    K_One = 6.68908545
    K_Two = 6.5630592
    Mosc = 0.3457

'''
import math
import numpy as np
import matplotlib.pyplot as plt

Data = np.load('../Datas/DampData.npy')
#Data = np.load("/Users/baiyang/Desktop/Workspace/Physics Lab/Damped Harmonic Oscillator/Datas/DampData.npy")

Yaxis_Xosc = Data[0:,1]
Xaxis_Time = Data[0:,0]

plt.xlabel("Time[s]")
plt.ylabel("Xosc(t)[m]")
plt.plot(Xaxis_Time,Yaxis_Xosc,"r",label='Experimental data')

from scipy.signal import find_peaks
peaks, _ = find_peaks(Yaxis_Xosc, height=0)


xpeak=Xaxis_Time[peaks]
ypeak=Yaxis_Xosc[peaks]

plt.plot(xpeak,ypeak,'b',label='Peaks Line')

def fit_func(x,k,b):
    return k*x+b

def fit_funcE(x,a,b):
    return a * np.exp(b*x)

from scipy.optimize import curve_fit

_popt,_ = curve_fit(fit_funcE, xpeak, ypeak)
_lY = [fit_funcE(i,*_popt) for i in xpeak]

popt,_ = curve_fit(fit_func, xpeak, ypeak)

lY = [fit_func(i, popt[0], popt[1]) for i in xpeak]

plt.figure(1)

plt.plot(xpeak,lY,'g',label = 'FC: Y=KX+b')
plt.plot(xpeak,_lY, 'y',label = 'FC: Y=A*exp(Bx)')

plt.legend()
plt.savefig('/Users/baiyang/Desktop/Workspace/Physics Lab/Damped Harmonic Oscillator/Datas/_fig3.5.png')
plt.show()

plt.figure(2)

diffs = ypeak - fit_func(xpeak,*popt)
zeroLine = np.zeros(len(xpeak))

plt.xlabel("Time[s]")
plt.ylabel("Xosc(t)[m]")
plt.plot(xpeak,diffs,'.',color = 'black')
plt.plot(xpeak,zeroLine,'r')

for i in range(len(xpeak)):
    LineX = (xpeak[i],xpeak[i])
    LineY = (0,diffs[i])
    plt.plot(LineX,LineY,'r')
plt.title('Diffs in Y=AX+b')
plt.savefig('/Users/baiyang/Desktop/Workspace/Physics Lab/Damped Harmonic Oscillator/Datas/_fig2.png')
plt.show()

plt.figure(3)

diffs = ypeak - fit_funcE(xpeak,*_popt)
zeroLine = np.zeros(len(xpeak))

plt.xlabel("Time[s]")
plt.ylabel("Xosc(t)[m]")
plt.plot(xpeak,diffs,'.',color = 'black')
plt.plot(xpeak,zeroLine,'r')

for i in range(len(xpeak)):
    LineX = (xpeak[i],xpeak[i])
    LineY = (0,diffs[i])
    plt.plot(LineX,LineY,'r')
plt.title('Diffs in Y=A*exp(Bx)')
plt.savefig('/Users/baiyang/Desktop/Workspace/Physics Lab/Damped Harmonic Oscillator/Datas/_fig3.png')
plt.show()
