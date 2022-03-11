a = 0

def show(n):
    global a
    if n <= 0:
        for i in range(a+1+n):
            print(i)
        return 0
    print(n)
    a += 2
    return show(n-2)

val = int(input("Enter n : \n"))
show(val)