'''
Homework 2
Q.1
a. Generate 11 even spaced data points using Runge function 𝑓(𝑥) = 1 over
range [-5:+5].
b. Then write a python code to carry out 10th order Lagrange interpolation for the generated data in part a.
c. Demonstrate the Runge phenomenon by plotting the interpolation function together with the data points.
d. Write a python code to carry cubic-Hermite interpolation for the generated data in part a, then plot the result function from the cubic-Hermite interpolation together with the data points.
NOTE: you must put your name in the title of the figure you plotted in part d.
Q.2
a.Generate 256 equally spaced data point susing function 𝑓(𝑥)=sin⁡(𝑥) over the x range [−4𝜋, +4𝜋], then add a noise (with range from -0.1 to +0.1) to the data. Plot the final data.
b. Carry out discrete Fourier transform to the data you obtained in a. Plot the frequency spectrum using the transformed data.
c. Explain the frequency spectrum you obtained.
NOTE: You must put your name in the legend of the frequency spectrum you obtained in part b.
1+𝑥2
'''

import matplotlib.pyplot as plt
import numpy as np 
import scipy.interpolate as itp

#Q1
plt.figure(1)
plt.xlabel('x values')
plt.ylabel('y values')
plt.title('999006125 Yang Bai')

#Part a
r_xNumbers = np.linspace(-5,5,11)
r_yNumbers = 1 / (1 + r_xNumbers**2)

#Part b
l_Tangents = itp.lagrange(r_xNumbers, r_yNumbers)

#Part c
plt.plot(r_xNumbers,r_yNumbers,'o',color='#581845',label='Original')
l_yNumbers = l_Tangents(r_xNumbers)
plt.plot(r_xNumbers,l_yNumbers,color='#F45F3F',label = 'Lagrange')

#Part d
ch_yNumberTangent = (-1) * ((2*r_xNumbers) / (1+r_xNumbers**2)**2)
ch_Tangents = itp.CubicHermiteSpline(r_xNumbers, r_yNumbers, ch_yNumberTangent)
ch_yNumbers = ch_Tangents(r_xNumbers)
plt.plot(r_xNumbers,ch_yNumbers,'--',color='#3F59F4',label = 'Cubic')
plt.legend()
plt.show()

#Q2
plt.figure(2)
plt.title('Question2')

#Part a
plt.subplot(2,1,1)
r_sxValues = np.linspace(-4*np.pi, 4*np.pi,256)
r_syValues = np.sin(r_sxValues)
noise = np.random.uniform(-0.1,0.1,1)
randomX = int(np.random.uniform(0,256,1))   #Highlight the noise point
noise_x = r_sxValues[randomX]
r_syValues[randomX] = noise
plt.plot(r_sxValues,r_syValues,'.',color='#990CF3',label='Original')
plt.plot(noise_x,noise,'.',color='#F30C63',label='Noise')
plt.legend()

#Part b 
plt.subplot(2,1,2)
T = np.pi*8/256
f_yValues = np.fft.fft(r_syValues)
f_xValues = np.fft.fftfreq(256, T)
print(f_xValues[randomX])
print(f_yValues[randomX])
plt.plot(f_xValues*2*np.pi,np.abs(f_yValues),color='#F87305',label='Yang Bai')
plt.legend()
plt.show()

#Part c
print("")