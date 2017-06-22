'''
Problem:
Given a binary tree, return all root-to-leaf paths.
For example, given the following binary tree:
   1
 /   \
2     3
 \
  5
All root-to-leaf paths are: ["1->2->5", "1->3"]
'''


# Recursive
class Solution:

    def binaryTreePaths(self, root):

        def helper(root, path, result):
            if not root:
                return

            # leaf node
            if not root.left and not root.right:
                path += str(root.val)
                result.append(path)
                return

            if root.left: helper(root.left,path+str(root.val)+"->",result)
            if root.right: helper(root.right,path+str(root.val)+"->",result)


        result = []
        if not root: return result
        helper(root,"",result)
        return result
        
     
     
     
# Iterative: BFS (queue)

import collections
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        if not root: return result
        
        q = collections.deque()
        q.append([root, str(root.val)])
        while len(q):
            node,path = q.popleft()
            if not node.left and not node.right:
                result.append(path[:])
            if node.left: 
                q.append([node.left, path + "->" + str(node.left.val)])
            if node.right:
                q.append([node.right, path + "->" + str(node.right.val)])
        return result
        
        

