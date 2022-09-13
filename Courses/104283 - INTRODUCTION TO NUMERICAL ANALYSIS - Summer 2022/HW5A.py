import numpy as np

def gauss(A, n):
    '''
    @noticed: 这是高斯法 (无主元), 不是作业要求的高斯部分主元法!!!! Algorithm6.1
    '''
    for i in range(0,n-1):
        for j in range(i+1, n):
            if A[n-1][n-1] != 0 :
                m = - A[j][i] / A[i][i]
                for k in range(0,n):
                    A[j][k] += A[i][k]*m
                A[j][-1] += A[i][-1]*m
            else:
                print("No unique Solution exist.")
                return False

    X = np.zeros(n)
    X[n-1] = A[n-1][-1] / A[n-1][n-1]

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            A[i][-1] -= A[i][j]*X[j]
        X[i] = A[i][-1] / A[i][i]

    return X

def gauss_elim_by_Row(A, n):
    '''
    @noticed 列主高斯消元法 不是作业要求!!! Algorithm6.2
    '''
    for i in range(0,n-1):

        val = A[i][i]
        nrow = i

        for j in range(i, n):
            if A[j][i] > val:
                val = A[j][i]
                nrow = j

        if val == 0:
            print("No unique solution exist.")
            return False

        if nrow != i:
            cache = [k for k in A[i]]
            A[i] = A[nrow]
            A[nrow] = cache

        for j in range(i+1, n):
            if A[n-1][n-1] != 0 :
                m = - A[j][i] / A[i][i]
                for k in range(0,n):
                    A[j][k] += A[i][k]*m
                A[j][-1] += A[i][-1]*m
            else:
                print("No unique Solution exist.")
                return False

    X = np.zeros(n)
    X[n-1] = A[n-1][-1] / A[n-1][n-1]

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            A[i][-1] -= A[i][j]*X[j]
        X[i] = A[i][-1] / A[i][i]

    return X

def gauss_elim(A, n):
    '''
    @noticed Homework solution. Algorithm6.3
    '''
    for i in range(n):
        if max(A[i][i:-1]) == 0:
            print("No unique solution exist.")
            return False
        val = np.abs(A[i][i]) / max(A[i][i:-1])
        nrow = i

        for j in range(i, n):
            caval = np.abs(A[j][i]) / max(A[j][j:-1])
            if caval > val:
                val = caval
                nrow = j

        if val == 0:
            print("No unique solution exist.")
            return False

        if nrow != i:
            cache = [k for k in A[i]]
            A[i] = A[nrow]
            A[nrow] = cache
        
        for j in range(i+1, n):
            if A[n-1][n-1] != 0 :
                m = - A[j][i] / A[i][i]
                for k in range(0,n):
                    A[j][k] += A[i][k]*m
                A[j][-1] += A[i][-1]*m
            else:
                print("No unique Solution exist.")
                return False
    
    X = np.zeros(n)
    X[n-1] = A[n-1][-1] / A[n-1][n-1]

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            A[i][-1] -= A[i][j]*X[j]
        X[i] = A[i][-1] / A[i][i]

    print("The solution matrix x is :")
    print(X)
    return X

def generate_Matrix(index = 1):
    cache = np.loadtxt("./system{}_A.txt".format(index))
    return cache

if __name__ == '__main__':
    #A = generate_Matrix(1)
    #print(gauss(A,len(A)))
    #print(gauss_elim_by_Row(A, len(A)))
    #gauss_elim(A, len(A))

    for i in range(1,5):
        A = generate_Matrix(i)
        print("---------------")
        print(f"System{i}_A.txt")
        print(f"A = {[j[0:-1].tolist() for j in A]}")
        print(f"b = {[j[-1] for j in A]}")
        gauss_elim(A, len(A))