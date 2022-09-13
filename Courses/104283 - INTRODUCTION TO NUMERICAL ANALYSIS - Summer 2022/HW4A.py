import numpy as np
import matplotlib.pyplot as plt
# Using numpy.linalg.solve instead of Algorithm6.7
class Spline:

    def __init__(self, x, y):
        self.b, self.c, self.d = [], [], []

        self.x = x
        self.y = y

        self.length = len(x)
        h = np.diff(x)

        self.a = [iy for iy in y]

        A = self.__generate__A(h)
        B = self.__generate__B(h)
        self.c = np.linalg.solve(A, B)

        for i in range(self.length - 1):

            self.d.append(
                (self.c[i + 1] - self.c[i]) / (3.0 * h[i])
            )

            self.b.append(
                (self.a[i + 1] - self.a[i]) / h[i] - h[i] * (self.c[i + 1] + 2.0 * self.c[i]) / 3.0
            )

    def get(self, p):

        assert self.x[0] <= p <= self.x[-1]

        i = self.__get_Index(p)
        dx = p - self.x[i]

        return self.a[i] + self.b[i] * dx + self.c[i] * dx ** 2.0 + self.d[i] * dx ** 3.0

    def __get_Index(self, x):
        for i in range(self.length):
            if self.x[i] - x > 0:
                return i - 1

    def __generate__A(self, h):

        A = np.zeros((self.length, self.length))

        A[0, 0] = 1.0
        A[0, 1] = 0.0
        A[self.length - 1, self.length - 2] = 0.0
        A[self.length - 1, self.length - 1] = 1.0

        for i in range(self.length - 1):
            if i is not self.length - 2:
                A[i + 1, i + 1] = 2.0 * (h[i] + h[i + 1])
            A[i + 1, i] = h[i]
            A[i, i + 1] = h[i]

        return A

    def __generate__B(self, h):
        
        B = np.zeros(self.length)
        for i in range(self.length - 2):
            B[i + 1] = 3.0 * (self.a[i + 2] - self.a[i + 1]) / h[i + 1] - 3.0 * (self.a[i + 1] - self.a[i]) / h[i]

        return B
    
    def showGragh(self, space=0.01):
        rx = np.arange(self.x[0],self.x[-1], space)
        ry = [self.get(i) for i in rx]

        plt.title("Cublic Spine")
        plt.plot(self.x, self.y, "x", label='Data points')
        plt.plot(rx, ry, "-", label = "Cubic Spine Result")
        plt.legend()
        plt.show()

if __name__ == '__main__':
    inx = np.loadtxt("./data_points_A.txt", usecols=0)
    iny = np.loadtxt("./data_points_A.txt", usecols=1)

    spline = Spline(inx, iny)
    spline.showGragh(0.01)