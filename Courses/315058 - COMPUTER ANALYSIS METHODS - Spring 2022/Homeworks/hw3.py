'''
Homework 3
Q.1
Carry out a LU decomposition of [1 −1 0], find the two triangular matrices
320 051
and the permutation matrix. Explain what does the permutation matrix do? And demonstrate the decomposition by showing the result of matrix products.
Q.2
Find the eigenvalues and eigenvectors of matrix [2 1] using 10 iterations of QR
12
decomposition. Plot the two diagonal elements of 𝐴𝑘 as a function of iteration
number k.
NOTE: you must put your name in the title of the 𝐴𝑘 plot.
Q.3
In the lecture, we saw that, in the scipy Newton (Newton Raphson) solver, the secant method is used if the first derivative of the function is not given in the parameters. Explain this connection between the secant method and the Newton method using necessary formula.
NOTE: You may need something from lecture 7.
'''

from scipy import linalg
import numpy as np
import matplotlib.pyplot as plt

'''
Q1

matrix_Given = [[3,2,0],
                [1,-1,0],
                [0,5,1]]

luResults = linalg.lu(matrix_Given)

print("Permutation Matrix : ")
print(luResults[0])

print("Lower Triangular Matrix : ")
print(luResults[1])

print("Upper Triangular Matrix : ")
print(luResults[2])

print("Result of the matrixs' product : ")
print((luResults[0].dot(luResults[1])).dot(luResults[2]))
'''

'''
Q2

matrix_Given = np.array([[2,1],
                [1,2]])

def getEigenValue(qrmatrix = np.array(0),depth = 1):
    if depth == 0:
        #return qrmatrix
        return qrmatrix.diagonal()
    mt = linalg.qr(qrmatrix)
    return getEigenValue(np.dot(mt[1],mt[0]),depth-1)

#print(getEigenValue(matrix_Given,11))

eigenValueList = []
for i in range(0,11):
    eigenValueList.append(getEigenValue(matrix_Given,i))

xValues = range(0, 11)
plt.title("Yang Bai 999006125")
plt.xlabel("Iterations")
plt.ylabel("EigenValue")
plt.xticks(range(0,11,1))
plt.plot(xValues, [3]*11, '--', label = 'Ture EigenValue',color='#F54325')
plt.plot(xValues, [1]*11, '--', label = 'Ture EigenValue',color='#F54325')
plt.plot(xValues,eigenValueList, color = '#6D73F2', label = 'Ak eigenvalues')
plt.plot(0 , 2, '.', color = '#F54325', label = 'Origin data')
plt.legend()
plt.show()
'''