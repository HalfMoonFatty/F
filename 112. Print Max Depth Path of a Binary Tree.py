
'''
Problem:

Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left),self.maxDepth(root.right))
        
        
        
        
# Follow-up: Print Max Depth Path of a Binary Tree

class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def maxDepthPath(root):

    def maxPath(root, path):
        if not root:
            return [0,'']
        left = maxPath(root.left, path)
        right = maxPath(root.right, path)
        if left[0] > right[0]:
            return (1+left[0], left[1]+str(root.val))
        else:
            return (1+right[0], right[1]+str(root.val))
    
    return maxPath(root, '')[1][::-1]


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n1.left = n2
n1.right = n3
n2.right = n4
n4.right = n5
n5.right = n6
n3.left = n7
print maxDepthPath(n1)

