s=input('Enter your string : \n')
def g(s,idx):
    if len(s)<3:
        return 0
    if ('0'<=s[0]<='9' and '0'<=s[1]<='9' and '0'<=s[2]<='9' and (s[0]<s[1]>s[2] or s[0]>s[1]<s[2]) and (idx+1)%(ord(s[1])-ord('0'))==0):
        return 1+g(s[1:],idx+1)
    return g(s[1:],idx+1)
def f(s):
    return g(s,0)
m=f(s)
print(m)

