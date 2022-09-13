import numpy as np

def LU_decomp(A):
    rows, columns = np.shape(A)
    if rows != columns:
        raise ValueError(
            f"'A' has to be of square shaped array but got a {rows}x{columns} "
            + f"array:\n{A}"
        )
    lower = np.zeros((rows, columns))
    upper = np.zeros((rows, columns))
    for i in range(columns):
        for j in range(i):
            total = 0
            for k in range(j):
                total += lower[i][k] * upper[k][j]
            lower[i][j] = (A[i][j] - total) / upper[j][j]
        lower[i][i] = 1
        for j in range(i, columns):
            total = 0
            for k in range(i):
                total += lower[i][k] * upper[k][j]
            upper[i][j] = A[i][j] - total
    return lower, upper

def LU_sol(A,b):
    L,U = LU_decomp(A)
    UX = []
    for i in range(len(b)):
        val = b[i]
        for j in range(0,i):
            val -= L[i][j]*UX[j]
        UX.append(val / L[i][i])
    
    X = np.zeros(len(UX))
    for i in range(len(UX)-1, -1, -1):
        val = UX[i]
        for j in range(len(UX)-1 , i-1, -1):
            val -= U[i][j] * X[j]
        X[i] = val / U[i][i]
    
    return X

def generate_Matrix(index = 1):
    cache = np.loadtxt("./system{}_B.txt".format(index))
    return cache

if __name__ == '__main__':
    for i in range(1,4):
        T = generate_Matrix(i)
        A = [j[0:-1].tolist() for j in T]
        b = [j[-1] for j in T]
        L, U = LU_decomp(A)
        print("---------------")
        print("System{}_B.txt".format(i))
        print(f"A = {A}")
        print(f"b = {b}")
        print("LU decomposition of matrix A:")
        print(f"Lower Matrix:\n{L}")
        print(f"Upper Matrix:\n{U}")
        print(f"L dot U equal to\n {np.dot(L,U)}")
        print(f"The solution is\n {LU_sol(A,b)}")
        