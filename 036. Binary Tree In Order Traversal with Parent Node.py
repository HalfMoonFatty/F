'''
Problem: Binary Tree In Order Traversal with Parent Node

class Node {Node left, Node right, Node parent}

Node getNext (Node current) {
} 
'''

'''
Solution:

Inorder --visite left -> root -> right

First check right child, if it's not null, then "the most left child of this right child" is the answer

Else check parent:

     if it is null, return null -- because this is the root and it is the last node in inorder

     if not, if node.parent.left = node (node is the left child of its parent), return parent

     if node.parent.right = node (node is the right child of its parent), go up and search ancester 
     
          if any ancester is the left child of its parent, return parent
          
          else return null

Time complexity:O(1) in average, worst O(h), 
space complexity: O(1)

'''


def findNext(root):
    if not root:
        return None
     
    if root.right:
        node = root.right
        while node.left:
            node = node.left
        return node

    elif not root.parent:
        return None

    elif root == root.parent.left:
        return root.parent

    elif root == root.parent.right: # search up until node is the left child or not parent node
        root = root.parent
        while root.parent and root.parent.right == root:
            root = root.parent
        return root.parent






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
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        stack = []
        result = []
        done = 0

        while not done:
            if root:
                stack.append(root)
                root = root.left 
            else:
                if len(stack):
                    root = stack.pop()
                    result.append(root.val)
                    root = root.right 
                else:
                    done = 1
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
