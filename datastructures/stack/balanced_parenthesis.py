# When doing this embrace modularization
# Iterate through the input and push all the opening parenthesis into stack
# When you encounter clossing parenthesis, pop the stack and check if it's a valid pair
#We create a class with a constructure function that used in modifying python list and the is_balanced flag


class  Parenthesis:
    def __init__(self):
        self.is_balanced_flag = True
        self.stack = []

    def is_balanced_parenthesis(self,paren):
        opening =['(','[','{']
        index=0
        while index<len(paren):
            if paren[index] in opening:
                self.stack.append(paren[index])
                index +=1
            else:
                if self.stack ==[]:
                    self.is_balanced_flag=False
                    break
                equivalent = self.stack.pop()
                if self.is_valid_pair(equivalent,paren[index]):
                    index +=1
                else:
                    self.is_balanced_flag = False
                    break
        if self.is_balanced_flag:
            print('valid')
        else:
            print('invalid')


    def is_valid_pair(self,o,c):
        if o=='(' and c==')':
            return True
        elif o=='[' and c==']':
            return True

        elif o=='{' and c=='}':
            return True
        else:
            return False

parenthesis = Parenthesis()
inputparen='({[{}()[]})'
parenthesis.is_balanced_parenthesis(inputparen)

