import numpy as np
import matplotlib.pyplot as plt

def mod_newton(p0, f, df, ddf, tol, max_iter):
    print("Modified Newton Method:")
    print("Inital guess p0 = " + str(p0))
    points = []

    for i in range(max_iter):
        if((df(p0)**2 - f(p0)*ddf(p0)) != 0):
            p = p0 - (f(p0)*df(p0) / (df(p0)**2 - f(p0)*ddf(p0)))
            points.append(p)

        if(np.abs(p - p0) < tol or (df(p0)**2 - f(p0)*ddf(p0)) == 0):
            print("Solution of f(x) = 0 is x = " + str(p))
            print("Iteration times is " + str(i+1))
            xCoordnates = np.linspace(p-1, p+1, max_iter)
            plt.plot(xCoordnates, f(xCoordnates), label = "Function", color = "#202C2C")
            plt.plot(points, np.zeros(len(points)), '.', label = "points", color = "#016471")
            plt.legend()
            plt.show()
            return p, i+1
            
        p0 = p

    print("Method failed after N0 iteration, N0 = " + str(max_iter))