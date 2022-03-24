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
a.Generate256equallyspaceddatapointsusingfunction 𝑓(𝑥)=sin⁡(𝑥) overthe x range [−4𝜋, +4𝜋], then add a noise (with range from -0.1 to +0.1) to the data. Plot the final data.
b. Carry out discrete Fourier transform to the data you obtained in a. Plot the frequency spectrum using the transformed data.
c. Explain the frequency spectrum you obtained.
NOTE: You must put your name in the legend of the frequency spectrum you obtained in part b.
1+𝑥2
'''

import matplotlib.pyplot as plt
import numpy as np 
