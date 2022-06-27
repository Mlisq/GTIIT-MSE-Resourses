import numpy as np 
import matplotlib.pyplot as plt
import scipy.optimize as op
import scipy.integrate as ite

#求一个1/4半径为1的圆的面积

rng = np.random.default_rng()               #Init Generator
points = rng.random((100,2))                #100个随机二维数组，值在0～1之间随机
hit = 0                                     #在圆中的数
total = 0                                   #总数组的数=100

for p in points:
    if p[0]*p[0]+p[1]*p[1] <= 1.0:
        hit += 1
    total += 1

print("The area of this pattern is:",end='')
print(hit/total)                            #我们取的样本数越多，这个值就越接近答案(pi/4)

'''
Monte-Carlo integration 就是将一条曲线近似为一个矩形，矩形的面积就是曲线的面积，即为积分。我们唯一需要做的就是求这个矩形的高（宽就是曲线的宽），
而高的值即曲线数学意义上的平均值。
'''