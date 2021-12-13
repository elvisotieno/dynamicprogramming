#Create Root


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                #null pointer check
                if self.left is None:
                    #create new node for the left
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data

    def contains_given_item(self,item):
        if item == data:
            return True
        elif item < self.data:
            if self.left is None:
                return False
            else:
                self.left.contains_given_item(item)
        else:
            if self.right is None:
                return False
            else:
                self.right.contains_given_item(item)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

root = Node(12)
root.insert(7)
root.insert(14)
root.insert(3)
root.print_tree()
print(root.contains_given_item(3))