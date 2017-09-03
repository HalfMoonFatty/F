'''
Problem:

Check if a tree is a subtree of another tree.

'''

# Time complexity: O(nk) -k nodes in subtree


class Solution(object):
    def isSubtree(self, s, t):

        def isValid(root1, root2):
            if not root1 and not root2:
                return True
            if not root1 or not root2:
                return False
            if root1.val == root2.val:
                return isValid(root1.right, root2.right) and isValid(root1.left, root2.left)
            return False
            
            
        if not s and not t:
            return True
        
        return s is not None and (isValid(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t))
                
