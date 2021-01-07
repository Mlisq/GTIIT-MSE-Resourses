def sort_2(a = []):
    return (a[::-1] if a[0] > a[1] else a)

def sort_3(a = []):
    a[:2] = sort_2(a[:2])
    a[1:] = sort_2(a[1:])
    a[:2] = sort_2(a[:2])
    return a

def sort_n(a = []):
    if len(a) == 2:
        return sort_2
    for i in range(len(a)):
        if(i+3>len(a)):
            break
        a[i:i+3] = sort_3(a[i:i+3])
        a[0:i+2] = sort_n(a[0:i+2])
    return a

val = input("Enter series : \n").split(' ')
a = [int(i) for i in val if i != '']
a = sort_n(a)
print(a)