times = 0
def check(n):
    global times
    end = n % 10
    if end % 2 == 0:
        times += 1
    if n // 10 == 0:
        if times % 2 != 0 and times != 0:
            return True
        return False
    return check(n // 10)

a = int(input("Enter n : \n"))
print(check(a))