#Assume all input will be legal
num = (int)(input("Enter n : \n"))

#Print the upper part
for i in range(num):
    for j in range(num - i - 1):
        print(' ',end = '')
        
    for j in range(2 * (i + 1) - 1):
        print('*',end = '')
    
    print('')
#Print the lower part
for i in range(num - 1, 0,-1): 
    for j in range(num - i):
        print(' ',end = '')
        
    for j in range(2 * i - 1):
        print('*',end = '')
    print('')