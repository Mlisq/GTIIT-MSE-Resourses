eventimes = 0
oddtimes = 0
def check(n):
    global eventimes
    global oddtimes
    end = n % 10
    if end % 2 == 0:
        eventimes += 1
    else:
        oddtimes += 1
    if n // 10 == 0:
        if (eventimes % 2 != 0 and oddtimes %2 == 0):
            return True
        return False
    return check(n // 10)

a = int(input("Enter n : \n"))
print(check(a))