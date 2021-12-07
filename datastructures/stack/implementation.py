# Stack is needed in keeping track of active functions or subroutines(recursion)
#Used in implementing DFS
#Implementation: We create a class with a constructure function that used in modifying python list

class Stack:
    def __init__(self):
        self.items = []

    # insert elements
    def push(self,item):
        self.items.append(item)

    #deleting item
    def pop(self):
        return self.items.pop()

    #checking if stack is empty
    def is_empty(self):
        return self.items==[]

    #accessing peack item
    def peak(self):
        if not self.is_empty():
            return self.items[-1]

    #seaching through the stack
    def search_stack(self,target):
        if not self.is_empty():
            return target in self.items
        else:
            return f"There's not {target} in the stack"

    #get snapshot of our stack
    def get_stack(self):
        return self.items

test_stack = Stack()

test_stack.push('Janet')
test_stack.push('Charles')
test_stack.push('Elvis')
test_stack.push('Brayan')
test_stack.pop()
print(test_stack.search_stack('Janet'))
print(test_stack.get_stack())

