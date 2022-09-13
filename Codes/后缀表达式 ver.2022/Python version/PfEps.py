class Postfix_Eps:

    result = []
    cache = []
    priority = {'+':1, '-':1, '*':2, '/':2,'^':3,'(':4}
    opreators = {'+':lambda a,b: b+a, '-':lambda a,b: b-a, '*':lambda a,b: b*a, '/':lambda a,b: b/a,'^':lambda a,b: b**a}

    def __init__(self, input = ""):
        flag = 0
        for index,i in enumerate(input):
            if(flag != 0 and index < flag):
                continue
            if i.isdigit():
                if index == len(input)-1:
                    self.result.append(i)
                else:
                    if index + 1 != len(input):
                        temp = i
                        index += 1
                        while(input[index].isdigit() and (index +1 < len(input))):
                            temp += input[index]
                            index += 1
                        if index == len(input)-1 and input[index].isdigit():
                            temp += input[index]
                            index += 1
                        self.result.append(temp)
                flag = index
            else:
                if len(self.cache) == 0:
                    self.cache.append(i)
                else:
                    if i == ')':
                        while self.cache:
                            if self.cache[-1] != '(':
                                self.result.append(self.cache.pop())
                            else:
                                self.cache.pop()
                                break
                        continue
                    if self.priority[i] > self.priority[self.cache[-1]]:
                        self.cache.append(i)
                    else:
                        if self.cache[-1] == '(':
                            self.cache.append(i)
                        else:
                            while self.cache:
                                if(self.priority[self.cache[-1]] >= self.priority[i]):
                                    self.result.append(self.cache.pop())
                                else:
                                    break
                            self.cache.append(i)
        
        while self.cache:
            self.result.append(self.cache.pop())

    def getExpression(self):
        re = ""
        for i in self.result:
            re += i
        return re

    def getResult(self):
        self.cache = []
        for i in self.result:
            if i.isdigit():
                self.cache.append(i)
            else:
                self.cache.append(self.opreators.get(i)(int(self.cache.pop()),int(self.cache.pop())))

        return int(self.cache[0])

if __name__ == '__main__':
    stri = input("Please input the expression, Press enter to finish entering.\n")
    ep = Postfix_Eps(stri)
    print("The postfix expression is: " + ep.getExpression())
    print("The result of the expression is: "+ str(ep.getResult()))