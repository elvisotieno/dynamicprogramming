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
        if self.data == item:
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

    # Inorder traversal
    # Left -> Root -> Right

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res


   # Preorder traversal
   # Root -> Left ->Right

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

root = Node(12)
root.insert(7)
root.insert(14)
root.insert(3)
root.insert(10)
root.insert(19)
root.insert(31)
root.print_tree()
print(root.inorder_traversal(root))
print(root.PreorderTraversal(root))