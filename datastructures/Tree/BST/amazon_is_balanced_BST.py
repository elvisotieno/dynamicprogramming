# Given a binary search tree you should determine if its balanced or not
#Balanced means the height of left and right subtree differ by no more than 1

#The idea: traversing the BST from bottom-up

#Defination for a binary tree node
from typing import Optional


class TreeNode:
    def __init__(self,value=0,left=None,right=None):
        self.value = value
        self.left = left
        self.right= right


class Solution:
    def is_balanced_BST(self,root: Optional[TreeNode])->bool:

        def dfs(root):
            #meaning the tree is empty
            if not root:
                return [True,0]

            #make few decision: Before we determine if the tree is balanced from the above root node
            #Fist we need to determine if from the left and the right subtree are balanced
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0] and abs(left[1]-right[1]) <= 1)

            return [balanced, 1 + max(left[1],right[1])]
        return dfs(root)[0]
