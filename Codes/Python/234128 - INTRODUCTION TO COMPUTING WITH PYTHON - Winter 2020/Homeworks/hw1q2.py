def isSymmetric(numberList = []):

    sum_1  = 0
    sum_2  = 0
    length = len((numberList))    
    
    for i in range(length):
        sum_1 += (10**(length-i-1))*numberList[i]
    
    for i in range(length,0,-1):
        sum_2 += (10**(i-1))*numberList[i-1]
        
    if(sum_2 == sum_1):
        return True
    else:
        return False

OddList  = []
EvenList = []
value    = input("Enter n : \n")

for i in range(len(value)):
    num = (int)(value[i])
    
    if(num % 2 == 0):
        EvenList.append(num)
    if(num % 2 != 0):
        OddList.append(num)

if(isSymmetric(OddList) and isSymmetric(EvenList)):
        print("both are symmetric")
elif(isSymmetric(OddList) and not isSymmetric(EvenList)):
        print("only odd is symmetric")
elif(not isSymmetric(OddList) and isSymmetric(EvenList)):
        print("only even is symmetric")
else:
        print("no sub number is symmetric")        
    