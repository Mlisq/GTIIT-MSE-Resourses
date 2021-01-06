def partition(a = []):
    pivot = 0
    index = pivot+1
    for i in range(index,len(a)):
        if a[i] < a[pivot]:
            a[i],a[index] = a[index], a[i]
            index += 1
    a[pivot],a[index-1] = a[index-1],a[pivot]
    return index

def quicksort(a):
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