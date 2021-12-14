#Creating a binary tree
class Node:

    def __init__(self, value):

        self.value = value

        self.left = None

        self.right = None

    def insert(self, value):

        if value:

            if value < self.value:

                if self.left is None:

                    self.left = Node(value)

                else:

                    self.left.insert(value)

            elif value > self.value:

                if self.right is None:

                    self.right = Node(value)

                else:

                    self.right.insert(value)

            else:

                self.value = value

#Let's insert elements into our binary search tree

root = Node(7)
root.insert(2)
root.insert(25)
root.insert(9)
root.insert(80)
root.insert(0)
root.insert(5)
root.insert(15)
root.insert(8)

#a recursive function that takes as input the root node and
# displays all the values in the tree in the ‘Depth First Search’ order.
def dfs_binary_tree(root):
    if root is None:

        return

    else:

        print(root.value, end=" ")

        dfs_binary_tree(root.left)

        dfs_binary_tree(root.right)

dfs_binary_tree(root)

