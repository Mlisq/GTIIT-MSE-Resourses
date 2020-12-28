
#Histogram Sort
def Histogramsort(x = [],minV = 0,maxV = 0):
    #Requirments: 数组必须全是整数，且知道其最大最小值
    #在满足题目条件情况下，我们可以得知数字的种类一共有 max-min+1 个 （相同的数字同一类）
    m = (maxV-minV) + 1
    #初始化histogram数组，作为相同数字的指标
    histogram = [0 for _ in range(m)]
    
    #histogram中每一个值代表该index指向的数字出现的数目
    '''
    Eg: Input >>> [1,3,4,4,2,3]
        histogram >>> [1,1,2,2]
        第一小的数字出现了一次 第二小的数字出现了一次 第三小的数字出现了两次 第四小的数字出现了2次
    '''
    for value in x:
        histogram[value-minV] += 1
    
    #我们要重新排序我们的数组，需要一个指标告诉我们排到哪了
    k = 0

    #一共有m种数，重复m次
    for i in range(m):
        #还记得histogram的含义吗
        '''
        Eg same as before : Input >>> [1,3,4,4,2,3]
                            histogram >>> [1,1,2,2]
        第一小的数字是1+0 出现了一次 所以我们循环一次 数组的第一个数字是1
        第二小同上
        第三小的数字是3+0 出现了两次 所以我们循环两次 数组的第三个和第四个数字是3
        第四小同上
        .....
        这里可能会有点绕，建议和代码的第16，17行一起看，尝试了解histogram的含义以及数字之间的关系
        '''
        for _ in range(histogram[i]):
            x[k] = i + minV
            k += 1

#Bubble Sort
def BubbleSort(list = []):
    #大的数像泡泡一样一点一点往上冒 顾名思义冒泡排序
    '''
    Eg: Input >>> [4,3,2,1]
    >>> [3,4,2,1]
    >>> [3,2,4,1]
    >>> [3,2,1,4]
    >>> [2,3,1,4]
    >>> [2,1,3,4]
    >>> [1,2,3,4]
    '''
    for i in range(len(list) - 1):
        for j in range(0,len(list)-i-1):
            if(list[j] > list[j+1]):
                list[j],list[j+1] = list[j+1],list[j]