import matplotlib.pyplot as plt
import numpy as np

MAX_ITEREATION_NUMBER = 50

def f(x):                                   
    return x-2**(-x)
    #return np.exp(x)-x**2+3*x-2
    #return 2*x*np.cos(2*x)-(x+1)**2
    #return x*np.cos(x)-2*(x**2)+3*x-1

def bisection(a, b, func, tol):
    points = []

    for i in range(MAX_ITEREATION_NUMBER):
        if a not in points: points.append(a)
        if b not in points: points.append(b)

        LR = func(a)
        p = a + (b-a)/2
        MR = func(p)

        if(MR == 0 or (b-a)/2 < tol):
            #Output result
            print("Solution of f(x) = 0 is x = " + str(p))
            print("Iteration times is " + str(i+1))
            #Plot the result
            xCoordnates = np.linspace(a-0.5, b+0.5, MAX_ITEREATION_NUMBER)
            plt.plot(xCoordnates, func(xCoordnates), label = "Function", color = "#202C2C")
            plt.plot(points, np.zeros(len(points)), '.', label = "Points", color = "#016471")
            plt.axhline(y = 0, linestyle = '--', color = "#438F5D", label = "y = 0")
            plt.legend()
            plt.show()
            return None

        if(LR * MR > 0):
            a = p
        else:
            b = p

    print("Method failed after N0 iteration, N0 = " + str(MAX_ITEREATION_NUMBER))

if __name__ == "__main__":
    bisection(0, 1, f, 1e-5)
