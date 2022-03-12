# Sorting
#recursion 递归 and divide and conquer分治
#Big O notation and Python's timeit module
array=[8,2,6,4,5]
sorted(array)
#Note: For a deeper dive into how Python's built-in sorting works,maybe I will talk...


# How to use sorted() and sort()in Python and Sorting Data With Python
# The Bubble Sort Algorithm in Python
def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
    return a
# The Bucket sort(historgram sort)
def historgramsort(x,minv,maxv):
    m=(maxv-minv)+1
    histogram=[0 for _ in range(m)]
    for value in x:
        histogram[value-minv]+=1
        k=0  # index in list(x)
        i=0  # index in histogram
        for i in range(m):
            for _ in range(histogram[i]):
                x[k]=i+minv
                k+=1
    return x
# mergesort 
def merge(list=[]):
    if (len(list)<2):
        return list
    mid = len(list)//2
    left= merge(list[:mid])
    right=merge(list[mid:])
    result=[]
    while left and right :
        if (left[0]<=right[0]):
            result.append(left.pop(0))
        else:result.append(right.pop(0))

    if left:
        result.extend(left)
    if right:
        result.extend(right)
    return result
   
# maxsort
def find_idx_of_max(l):
    max_idx=0
    for i in range(1,len(l)):  
        if l[i]>l[max_idx]:
            max_idx=i
    return max_idx
def maxsort(l):
    for end_idx in range(len(l)-1,0,-1):
        max_idx=find_idx_of_max(l[:end_idx+1])
        l[max_idx],l[end_idx]=l[end_idx],l[max_idx]
    return l

# Strings' characters
name='technion'
name[2:6:2] # >>> 'cn'
name.find('ion') # >>> 5 记得是从0开始数
name.find('abcd')# >>> -1 如果没找到就显示-1
s='Red Green Bule'
color_list=s.split(" ") # >>> ['Red','Green','Bule']
sep=';'
sep.join(color_list) # >>>'Red;Green;Blue'
# 我们只能将字符串加入到列表里面，而不能将列表加入到字符串里面
#但是最后我们的结果是得到字符串

#split 将一个指定目标从 ‘字符串’里 除去后形成一个列表
sentence='you connot end a sentence with because because is a conjunction.'
sentence.split('because') # >>>['you cannot end a sentence with ',' ',' ',' ','is a conjunction.']

#字符串可以replace函数达到替换的目的
s='hello world!'
s.replace('Hello','Goodbye') # >>> 'Goodby world!'

# 只有在range里才可以用这种形式表示slicing(1,3,2),其他都得用这种形式(1:3:2)
# my_list[strat:end:step] items start through end -1, by step

# insert 插入列表,也可以是字符串（在开头）
# append 插入列表,也可以是字符串（在末尾）
# extend 插入列表中的每一个元素 （在末尾）
# remove 移除列表中的一个元素

#创建一个矩阵
rows=int(input('enter number of rows:'))
matrix=[]
for i in range(rows):
	row=input('enter row'+str(i)+':')
	my_list=row.split(' ')
	matrix.append(my_list)
print(matrix)

# 检查一个数是否为质数
import math
from unittest import result
from xml.dom.expatbuilder import ExpatBuilderNS # 导入math函数库
n=int(input('please enter a number'))
if n==1:
    print('1 is not prime')
elif n!=2 and n%2 ==0:
    print(n,'equals',2,*n//2)
else:
    for div in range (3,int(math.sqrt(n))+1,2):
        if n%div==0:
            print(n,'equals',div,'*',n//div)
            break
        else:
            print(n,'is a prime number')

# 如何找到矩阵具有一定特征的数字
def check_matrix(n):
    return len([1 for i in range(len(n)) for j in range(len(n[0])) if (n[i][j])%2!=0])
print(check_matrix([[1,2,3,4],[2,3,4,5]]))

# merge 
def merge(a,b): # a is sorted,b is sorted
    c=[0 for _ in range (len(a))+len(b)]
    ia,ib,ic =0,0,0
    while ia<len (a) and ib<len(b):
        if a[ia]<=b[ib]:
            c[ic]=a[ia]
            ia+=1
        else:
            c[ic]=b[ib]
            ib+=1
        ic+=1
        for i in range(ia,len(a)):
            c[ic]=a[ia]
            ia,ic=ia+1,ic+1
        for i in range(ib,len(b)):
            c[ic]=b[ib]
            ib,ic = ib+1,ic+1
    return c

# How not to use 'is' operator
a=256
b=256
a is b # True
a=257
b=257
a is b # False
# Explatnion:当你启动Python 的时候,  数值为 -5 到 256 的对象就已经被分配好了. 
# 这些数字因为经常被使用, 所以会被提前准备好.
#当 a 和 b 在同一行中被设置为 257 时, Python 解释器会创建一个新对象, 然后同时引用第二个变量.
#如果你在不同的行上进行, 它就不会 "知道" 已经存在一个 257 对象了
# is 运算符检查两个运算对象是否引用自同一对象 (即, 它检查两个运算对象是否相同).
# == 运算符比较两个运算对象的值是否相等.


#a += b 并不总是与 a = a + b 表现相同. 类实现 op= 运算符的方式 也许 是不同的, 列表就是这样做的.
#表达式 a = a + [5,6,7,8] 会生成一个新列表, 并让 a 引用这个新列表, 同时保持 b 不变.
#表达式 a += [5,6,7,8] 实际上是使用的是 "extend" 函数, 所以 a 和 b 仍然指向已被修改的同一列表.
a = [1, 2, 3, 4]
b = a
a = a + [5, 6, 7, 8]
# >>> a=[1, 2, 3, 4, 5, 6, 7, 8]
# >>> b=[1, 2, 3, 4]
a = [1, 2, 3, 4]
b = a
a += [5, 6, 7, 8]
# >>> a=[1, 2, 3, 4, 5, 6, 7, 8]
# >>> b=[1, 2, 3, 4, 5, 6, 7, 8]


# 如何适用lambda和filter检查一个已经排好序的列表是否是等差数列
def check_ari_prog(list_var):
    possible_diff=list_var[1]-list[0]
    first_value=list_var[0]
    compared_results=[(list_value,first_value+(list_index*possible_diff))for list_index,list_value in enumerate(list_var)]
    result_list=list(filter(lambda x: x[0]==x[1],compared_results))
    return len(list_var)==len(result_list)

#binarysearch 
def binarySearch(my_list,x):
   i,j=0,len(my_list)-1
   while i<=j:
        m=(i+j)//2
        if my_list[m]==x:
            return m
        if my_list[m]<x:
            i=m+1
        else:
            j=m-1


# list 不能 用 .find(), 但可以用 count
# strip 不会关心顺序，但是一遇到无法去除的字符串就会停下
