import numpy as np
import matplotlib.pyplot as plt

def LS(xs, ys, degree):
    '''
    Copied from lv
    '''
    b = np.zeros(degree+1)
    temp = np.zeros(len(xs))
    a = [np.zeros(degree+1) for _ in range(degree+1)]
    for i in range(degree+1):
        for j in range(len(xs)):
            temp[j] = (xs[j]**i)*ys[j]
        b[i] = np.sum(temp)
        for l in range(degree+1):
            for j in range(len(xs)):
                temp[j] = xs[j]**(i+l)
            a[i][l] = np.sum(temp)
    coeff = np.linalg.solve(a,b)
    E = 0
    for k in range(len(xs)):
        xarr = []
        for d in range(degree+1):
            xarr.append(xs[k]**d)
        E += (ys[k]-coeff.dot(np.array(xarr).T))**2
    return coeff,E

if __name__ == '__main__':
    inx = np.loadtxt("./data_points_B.txt", usecols=0)
    iny = np.loadtxt("./data_points_B.txt", usecols=1)
    outx =  np.arange(inx[0], inx[-1], 0.01)

    plt.plot(inx, iny, '.', label='Origin data')
   
    coeffsa = LS(inx, iny ,1)
    outya = [(coeffsa[0][0]+coeffsa[0][1]*i) for i in outx]
    plt.plot(outx, outya, label='Linear')
    print("Error of Linear is :")
    print(coeffsa[1])
    print('----------------')
    coeffsb = LS(inx, iny ,2)
    outyb = [(coeffsb[0][0]+coeffsb[0][1]*i+coeffsb[0][2]*i**2) for i in outx]
    plt.plot(outx, outyb, label='2nd order')
    print("Error of 2nd order is :")
    print(coeffsb[1])
    print('----------------')

    coeffsc = LS(inx, iny ,3)
    outyc = [(coeffsc[0][0]+coeffsc[0][1]*i+coeffsc[0][2]*i**2+coeffsc[0][3]*i**3) for i in outx]
    plt.plot(outx, outyc, label='3rd order')
    print("Error of 3rd order is :")
    print(coeffsc[1])

    plt.legend()
    plt.show()
