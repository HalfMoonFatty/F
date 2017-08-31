'''
Problem:
Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:
    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.
'''


# Recursive

import sys
class Solution(object):
    def isValidBST(self, root):
    
        def validBST(root, minVal, maxVal):
            if not root:
                return True
            if root.val >= maxVal or root.val <= minVal:
                return False
            return validBST(root.left, minVal, root.val) and validBST(root.right, root.val, maxVal)

        return validBST(root, -sys.maxint+1, sys.maxint)
        
        
# Iterative

def inorder(root):

    def pushLeft(node):
        while node:
            stack.push(node)
            node = node.left
        return

    if not root: return True

    stack = []
    previous = -sys.maxint-1
    pushLeft(root)
    while len(stack):
        cur = stack.pop()
        if previous >= cur.val:
            return False
        previous = cur.val
        if cur.right:
            pushLeft(cur.right)
    return True
