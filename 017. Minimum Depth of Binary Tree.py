'''
Problem:

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''


# Solution 1: Recursive

class Solution(object):
    def minDepth(self, root):

        if root is None:
            return 0
        # still need to go left
        if root.left and not root.right:
            return 1+self.minDepth(root.left)
        # still need to go right
        if root.right and not root.left:
            return 1+self.minDepth(root.right)
        else:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
            
            
# Solution 2: Iterative

def minDepth(root):
    if not root: return 0

    q = collections.deque()
    q.append(root)
    level = result = 0
    while result == 0:
        level += 1
        for i in range(len(q)):
            cur = q.popleft()
            if not cur.left and not cur.right:
                result = level
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    return result

