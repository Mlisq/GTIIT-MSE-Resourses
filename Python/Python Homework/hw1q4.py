from copy import deepcopy

def checkSpace(List = []):

    _List = deepcopy(List)

    for i in List:
        if i == '':
            _List.remove(i)

    return _List

def checkQualified(List = [], Index = 0, ValueX = 0, sumForNow = 0):
    
    Length = len(List)

    if(((int)(List[Index]) + sumForNow) > ValueX):
        return False
    
    if (((int)(List[Index]) + sumForNow) == ValueX):
        return True
    else:
        if Index + 1 == Length:
            return False
        return checkQualified(List, Index + 1, ValueX, sumForNow + (int)(List[Index]))

seriesList = checkSpace(input("Enter series : ").split(' '))

X    = int(input("Enter x : "))
Flag = False

for i in range(len(seriesList)):
    if(checkQualified(seriesList , i , X , 0)):
        print("can be found starting in location %d "%i)
        Flag = True
        break

if not Flag :
    print("can NOT be found")

print('')