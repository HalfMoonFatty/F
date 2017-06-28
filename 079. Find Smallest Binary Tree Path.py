'''
Problem:

Given a binary tree, find the smallest path among all path in the tree.

     5
    / \
  10   3
 / \  /
1  7 8

路径有： 5 10 1   5 10 7   5 3 8     
排序后： 1 5 10   5 7  10  3 5 8 
所以按字符串类型排序为： 1 5 10 < 3 5 8 < 5 7 10

Time need to be linear
'''

'''
Solution:

本题就是找到最小值所在的那条路径然后返回

Time: O(n) 每个node都访问一遍

'''


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



import sys
def findSmallPath(root):
    def helper(root):
        if not root:
            return [sys.maxint, '']
        if not root.left and not root.right:
            return [root.val, str(root.val)]
        else:
            left = helper(root.left)
            right = helper(root.right)
            path = str(root.val)
            if left[0] > right[0]:
                path += right[1]
            else:
                path += left[1]
            minVal = min(root.val, min(left[0], right[0]))

            return [minVal, path]

    return helper(root)[1]



root = TreeNode(5)
n1 = TreeNode(10)
n2 = TreeNode(3)
n3 = TreeNode(1)
n4 = TreeNode(7)
n5 = TreeNode(8)

root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5

print findSmallPath(root)

