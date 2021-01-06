def max_even(a = []):
    maximum = a[0]
    for i in range(len(a)):
        if(a[i] >= maximum):
            maximum = a[i]
            if(i+2>len(a)):
                return maximum
            if(a[i+1] < a[i]):
                return maximum
    return 0

val = input("Enter your mountain : \n").split(' ')
a = [int(i) for i in val if i != '']
if(len(a) == 0):
    print("empty mountain")
else:
    print(max_even(a))