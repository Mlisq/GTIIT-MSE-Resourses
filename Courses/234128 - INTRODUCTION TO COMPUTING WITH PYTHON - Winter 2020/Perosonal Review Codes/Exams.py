'''Exam 3
'''
def fff1(m = {}):
    return {m[i]:i for i in m.keys()}

def fff2(my_lists = []):
    return [my_lists[i//2] for i in range(2*len(my_lists))]

def fff3(strings = ""):
    s1 = set(strings)
    s2 = set("abcedfghijklmnopqrstuvwxyz")
    s3 = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    #print({chr(ord(x)-ord('a')+ord('A')) for x in s1&s2})
    return {str(i).upper() for i in s1&s2} == s1&s3

def fff4(n):
    for _ in range(n):
        for _ in range(n):
            print(1)
            continue 
        else:
            print(0)
            break
'''Exam 1
'''
def f2(s,c1,c2):
    return "".join([i if i != c2 else c1+i for i in list(s)])
    
def f3(a,x):
    pass

def f31(a):
    return True if len(set(a)) == 1 else False

def f4(n):
    return [[int(j == i) or int(n-j-1 == i) for j in range(n)] for i in range(n)]