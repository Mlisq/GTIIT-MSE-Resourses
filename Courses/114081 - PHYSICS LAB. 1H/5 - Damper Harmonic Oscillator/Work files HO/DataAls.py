import numpy as np
''' Data
#data = np.load("../Datas/Data.npy")
data = np.load("/Users/baiyang/Desktop/Workspace/Physics Lab/Damped Harmonic Oscillator/Datas/Data.npy")

Yaxis_Xosc = data[0:,1]
Xaxis_Time = data[0:,0]

from scipy.signal import find_peaks
peaks, _ = find_peaks(Yaxis_Xosc, height=0)
xpeak=Xaxis_Time[peaks]
ypeak=Yaxis_Xosc[peaks]

def fit_func(x,k,b):
    return k*x+b

from scipy.optimize import curve_fit
popt,_ = curve_fit(fit_func, xpeak, ypeak)

diffs = ypeak - fit_func(xpeak,*popt)
print(popt)

sumsquare = 0
for i in range(len(diffs)):
    sumsquare += diffs[i]**2
SSE = sumsquare

_diffs = np.average(ypeak) - fit_func(xpeak,*popt)

sumsquare = 0
for i in range(len(_diffs)):
    sumsquare += _diffs[i]**2
SST = sumsquare

R = 1- (SSE/SST)

print(R)
'''
#'''
data = np.load("/Users/baiyang/Desktop/Workspace/Physics Lab/Damped Harmonic Oscillator/Datas/DampData.npy")

Yaxis_Xosc = data[0:,1]
Xaxis_Time = data[0:,0]

from scipy.signal import find_peaks
peaks, _ = find_peaks(Yaxis_Xosc, height=0)
xpeak=Xaxis_Time[peaks]
ypeak=Yaxis_Xosc[peaks]
lypeak = np.log(ypeak)

def fit_func(x,a,b):
    return np.log(a)+b*x

from scipy.optimize import curve_fit
popt,_ = curve_fit(fit_func, xpeak, lypeak)
print(popt)
diffs = lypeak - fit_func(xpeak,*popt)

sumsquare = 0
for i in range(len(diffs)):
    sumsquare += diffs[i]**2
SSE = sumsquare

sumsquare = 0
_diffs = np.average(lypeak) - fit_func(xpeak,*popt)

for i in range(len(_diffs)):
    sumsquare += _diffs[i]**2
SST = sumsquare

R = 1- (SSE/SST)

print(R)
#'''