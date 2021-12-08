# We need to keep track of the remainder while updating the divident and the divisor

class GCD:
    def __init__(self):
        self.stack=[]
    def get_gcd_two_numbers(self, num1, num2):
        divident = max(num1,num2)
        divisor = min(num1,num2)
        if divident ==0:
            return divisor
        elif divisor ==0:
            return divident
        else:
            remainder = divident%divisor
            while remainder>0:
                self.stack.append(remainder)
                divident = divisor
                divisor = remainder
                remainder=divident%divisor
            return self.stack.pop()
    def lcm(self,num1,num2):
        gcd= self.get_gcd_two_numbers(num1,num2)
        return (num1*num2)//gcd
gcd= GCD()
print(f'The GCD is:{gcd.get_gcd_two_numbers(24,60)}')
print(f'The LCM is: {gcd.lcm(24,60)}')
