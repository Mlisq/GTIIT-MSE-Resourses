def f1(m = {}):
    return {m[i]:i for i in m.keys()}

def f2(my_lists = []):
    return [my_lists[i//2] for i in range(2*len(my_lists))]

def f3(strings = ""):
    s1 = set(strings)
    s2 = set("abcedfghijklmnopqrstuvwxyz")
    s3 = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    #print({chr(ord(x)-ord('a')+ord('A')) for x in s1&s2})
    return {str(i).upper() for i in s1&s2} == s1&s3

def f4(n):
    for _ in range(n):
        for _ in range(n):
            print(1)
            continue 
        else:
            print(0)
            break
