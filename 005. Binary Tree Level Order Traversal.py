'''
Problem:

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
     For example:
     Given binary tree {3,9,20,#,#,15,7},
         3
        / \
       9  20
         /  \
        15   7
     return its level order traversal as:
     [
     [3],
     [9,20],
     [15,7]
     ]
'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Solution 1: Recursive

class Solution(object):
    def levelOrder(self, root):

        def helper(root, level, result):

            if not root:
                return

            if level == len(result):
                result.append([])

            result[level].append(root.val)
            helper(root.left,level+1,result)
            helper(root.right,level+1,result)

        result = []
        helper(root,0,result)
        return result




# Solution 2: Iterative

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: 
            return []
        
        result = []
        q = collections.deque([root])
        while len(q):
            size = len(q)
            result.append([])
            for i in range(size):
                cur = q.popleft()
                result[-1].append(cur.val)
                if cur.left: q.append(cur.left)
                if cur.right: q.append(cur.right)
        return result
