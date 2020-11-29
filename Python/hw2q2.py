def isSymmetric(numberList = []):
    #Simplist way: Just check if the number made from left to right equals to one made from right to left
    
    sum_1 = 0
    sum_2 = 0
    length = len((numberList))    #To save some memory XD
    
    for i in range(length):
        sum_1 += (10**(length-i-1))*numberList[i]
    
    for i in range(length,0,-1):
        sum_2 += (10**(i-1))*numberList[i-1]
        
    if(sum_2 == sum_1):
        return True
    else:
        return False
    
    return False

#----int main(){----#

OddList = []
EvenList = []

value = input("Input your numbers : ")

#Classfiy types
for i in range(len(value)):
    num = (int)(value[i])
    
    if(num % 2 == 0):
        EvenList.append(num)
    if(num % 2 != 0):
        OddList.append(num)

#Judge. Ps: WHY THIS LANUAGE DON'T HAVE '&&' OR '||' ?
if(isSymmetric(OddList) and isSymmetric(EvenList)):
        print("Both are symmetric")
elif(isSymmetric(OddList) and not isSymmetric(EvenList)):
        print("Only Odd part is symmetric")
elif(not isSymmetric(OddList) and isSymmetric(EvenList)):
        print("Only Even part is symmetric")
else:
        print("No sub number is symmetric")
        
#----return 0;}----#
    