'''
Problem: Preorder Traversal

Given a binary tree, return the preorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
     1
      \
       2
      /
     3
return [1,2,3].
Note: Recursive solution is trivial, could you do it iteratively?
'''

# Iterative
class Solution:

    def preorderTraversal(self, root):

        if not root:
            return []

        result = []
        stack = [root]

        while len(stack):
            root = stack.pop()
            res.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)

        return result
        
        


# Recursive

class Solution(object):

    def preorderTraversal(self, root):

        def preHelper(root, result):
            if not root:
                return

            result.append(root.val)
            preHelper(root.left,result)
            preHelper(root.right,result)
            return

        result = []
        preHelper(root, result)
        return result
        
        
        
'''
Problem: Inorder Traversal

Given a binary tree, return the inorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
     1
       \
        2
       /
      3
return [1,3,2].
Note: Recursive solution is trivial, could you do it iteratively?
'''

# Iterative

class Solution(object):

    def inorderTraversal(self, root):

        if not root: return []

        result = []
        stack = [root]

        while len(stack) > 0:
            if root:            # go to the left most node
                stack.append(root.left)
                root = root.left
            else:
                stack.pop()     # pop out None
                if len(stack) > 0:
                    root = stack.pop()
                    result.append(root.val)
                    stack.append(root.right)    # go right
                    root = root.right
                else:
                    break
        return result
        
        

# Recursive

class Solution(object):
    def inorderTraversal(self, root):

        def inorderHelper(root,result):
            if not root:
                return result
            inorderHelper(root.left,result)
            result.append(root.val)
            inorderHelper(root.right,result)

        result = []
        inorderHelper(root,result)
        return result
        
        
        
'''
Problem: Postorder Traversal

Given a binary tree, return the postorder traversal of its nodes' values.
For example:
Given binary tree {1,#,2,3},
     1
      \
       2
      /
     3
return [3,2,1].
Note: Recursive solution is trivial, could you do it iteratively?
'''


# Iterative

class Solution(object):

    def postorderTraversal(self, root):

        if not root: return []

        result = []
        stack = [root]
        while len(stack):
            if root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            # 拐弯 
            else:
                root = stack.pop()          # remember root
                if stack and root.right and root.right == stack[-1]:
                    right = stack.pop()     # pop out right child
                    stack.append(root)
                    root = right
                else:
                    result.append(root.val)
                    root = None
                    
        result.pop() # because we init stack as [root]
        return result
        
        



# Recursive

class Solution(object):

    def postorderTraversal(self, root):

        def postHelper(root, result):
            if not root:
                return
            postHelper(root.left,result)
            postHelper(root.right,result)
            result.append(root.val)
            return

        result = []
        postHelper(root,result)
        return result
