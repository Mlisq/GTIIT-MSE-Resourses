import numpy as np
import matplotlib.pyplot as plt

MAX_ITERATION_NUMBER = 100
TOLERANCE = 1e-5

def fixer_point(p0, g, tol, max_iter):

    p_list = []

    for i in range(max_iter):
        p = g(p0)
        if abs(p - p0) < tol:
            print("Solution of p = g(p) is p = " + str(p))
            print("Iteration times is " + str(i+1))
            xCoordnates = np.linspace(p-0.5, p+0.5, max_iter)
            plt.plot(xCoordnates, g(xCoordnates), label = "Function", color = "#202C2C")
            plt.axhline(y = p, color = "#438F5D", label = "Final p")
            for pi in p_list:
                plt.axhline(y = pi, linestyle = '--', color = "#016471")
            plt.legend()
            plt.show()
            return p
        p_list.append(p)
        p0 = p
    else:
        print("We could not find a solution")

def steffenson(p0, g, tol, max_iter):

    p_list = []

    for i in range(max_iter):

        p1 = g(p0)
        p2 = g(p1)
        p = p0 - ((p1 - p0)**2) / (p2 - 2*p1 + p0)

        if abs(p - p0) < tol:
            print("Solution of p = g(p) is p = " + str(p))
            print("Iteration times is " + str(i+1))
            xCoordnates = np.linspace(p-0.5, p+0.5, max_iter)
            plt.plot(xCoordnates, g(xCoordnates), label = "Function", color = "#202C2C")
            plt.axhline(y = p, color = "#438F5D", label = "Final p")
            for pi in p_list:
                plt.axhline(y = pi, linestyle = '--', color = "#016471")
            plt.legend()
            plt.show()
            return p
        
        p_list.append(p)
        p0 = p

    else:
        print("We could not find a solution")

def g(x):
    #return (2 - np.exp(x) + x**2)/3                     #0~1
    #return 0.5*(np.sin(x)+np.cos(x))                    #0~1
    #return np.sqrt(np.exp(x)/3)                         #0~1 3~4
    return 5**(-x)                                      #0~1

if __name__ == "__main__":
    fp = fixer_point(0.5, g, TOLERANCE, MAX_ITERATION_NUMBER)
    sf = steffenson(0.5, g, TOLERANCE, MAX_ITERATION_NUMBER)

    assert fp - g(fp) < TOLERANCE
    assert sf - g(sf) < TOLERANCE

    print("Test Successful")
