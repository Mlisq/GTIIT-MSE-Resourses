def partition(a = []):
    point = 0
    for i in range(len(a)):
        if(a[point] < a[i]):
            a[point], a[i] = a[i], a[point]
            point = i
    return point+1

def quicksort(a = []):
    if len(a) < 2 :
        return a
    i = partition(a)
    a[:i] = quicksort(a[:i])
    a[i:] = quicksort(a[i:])
    return a

val = input("Enter numbers : \n").split(' ')
a = [int(i) for i in val if i != '']
a = quicksort(a)
print(a)

