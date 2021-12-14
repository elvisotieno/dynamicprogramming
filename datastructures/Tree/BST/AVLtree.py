#1)creating the node class


class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.height = 1


#2)Define the AVL class

class AVL:
    #2.0) define height function which returns the height of a node
    def height(self,node):
        if node is None:
            return 0
        else:
            return node.height

    #2.1) calculate balancing factor
    def balance(self, node):
        if node is None:
            return 0
        else:
            return self.height(node.left) - self.height(node.right)

    #2.2)find the empty node
    def MinimumValueNode(self, node):
        if node is None or node.left is None:
            return node
        else:
            return self.MinimumValueNode(node.left)


    #2.3) Defining the Right Rotation Method used to rotate the Tree in the clock-wise direction
    def rotateR(self, node):
        a = node.left
        b = a.right
        a.right = node
        node.left = b
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    #2.4)Defining the Left Rotation Method used to rotate the Tree in the anti-clockwise direction
    def rotateL(self, node):
        a = node.right
        b = a.left
        a.left = node
        node.right = b
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))
        return a

    #2.5)Defining the insert() method which is used to insert elements into the AVL Tree

    def insert(self, val, root):
        if root is None:
            return Node(val)
        elif val <= root.value:
            root.left = self.insert(val, root.left)
        elif val > root.value:
            root.right = self.insert(val, root.right)
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)
        if balance > 1 and root.left.value > val:
            return self.rotateR(root)
        if balance < -1 and val > root.right.value:
            return self.rotateL(root)
        if balance > 1 and val > root.left.value:
            root.left = self.rotateL(root.left)
            return self.rotateR(root)
        if balance < -1 and val < root.right.value:
            root.right = self.rotateR(root.right)
            return self.rotateL(root)
        return root


    #2.6)Defining the delete() method which is used to delete elements from the AVL Tree
    def delete(self, val, node):
        if node is None:
            return node
        elif val < node.value:
            node.left = self.delete(val, node.left)
        elif val > node.value:
            node.right = self.delete(val, node.right)
        else:
            if node.left is None:
                lt = node.right
                node = None
                return lt
            elif node.right is None:
                lt = node.left
                node = None
                return lt
            rgt = self.MinimumValueNode(node.right)
            node.value = rgt.value
            node.right = self.delete(rgt.value, node.right)
        if node is None:
            return node
        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)
        if balance > 1 and self.balance(node.left) >= 0:
            return self.rotateR(node)
        if balance < -1 and self.balance(node.right) <= 0:
            return self.rotateL(node)
        if balance > 1 and self.balance(node.left) < 0:
            node.left = self.rotateL(node.left)
            return self.rotateR(node)
        if balance < -1 and self.balance(node.right) > 0:
            node.right = self.rotateR(node.right)
            return self.rotateL(node)
        return node

    