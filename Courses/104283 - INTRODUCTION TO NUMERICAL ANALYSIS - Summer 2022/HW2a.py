import numpy as np
import matplotlib.pyplot as plt

def newton(p0, f, df, tol, max_iter):

    print("Inital p0 = " + str(p0))
    midpoints = []

    for i in range(max_iter):

        p = p0 - (f(p0) / df(p0))
        midpoints.append(p)

        if(np.abs(p - p0) < tol):
            print("Solution of f(x) = 0 is x = " + str(p))
            print("Iteration times is " + str(i+1))
            xCoordnates = np.linspace(p-5, p+5, max_iter)
            plt.plot(xCoordnates, f(xCoordnates), label = "Function", color = "#202C2C")
            plt.plot(midpoints, np.zeros(len(midpoints)), '.', label = "MidPoints", color = "#016471")
            plt.legend()
            plt.show()
            return p, i+1
            
        p0 = p

    print("Method failed after N0 iteration, N0 = " + str(max_iter))