#We divide by two and append the remainder in stak
# once the qoutient is 0 we pop elements from our stack and concatnate with an empty string
#We create a class with a constructure function that used in modifying python list(stack) and Quatient

class IntegerToBinary:
    def __init__(self):
        self.stack = []
    #recursive approach
    def interger_to_binary(self,num):
        quatient = num

        def recursion(quatient):
            if quatient==0:
                return self.stack
            else:
                self.stack.append(quatient % 2)
                quatient=quatient//2
                recursion(quatient)
        recursion(quatient)
        binary=''
        while len(self.stack)>0:
            binary+=(str(self.stack.pop()))
        return binary


decimalconerter=IntegerToBinary()
print(decimalconerter.interger_to_binary(1000))

class IntegerToBinary:
    def __init__(self):
        self.stack = []
    #recursive approach
    def interger_to_binary_iterations(self,num):
        quatient = num

        while quatient>0:
            self.stack.append(quatient % 2)
            quatient=quatient//2

        binary=''
        while self.stack !=[]:
            binary+=(str(self.stack.pop()))
        return binary


decimalconerter=IntegerToBinary()
print(decimalconerter.interger_to_binary_iterations(80))

