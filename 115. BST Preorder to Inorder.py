'''
Problem:

给一个BST的先序遍历结果，返回中序遍历结果。

讨论各种做法，复杂度。

'''


def preOrderToInOder(preorder):
    
    if not preorder: return []

    result = []
    stack = []
    for n in preorder:
        while len(stack) and n > stack[-1]:
            result.append(stack.pop())

        stack.append(n)
        #print stack, result
    result.append(stack.pop())
    return result

preorder = [5,2,1,4,6,7]
print preOrderToInOder(preorder)




'''
Problem: Verify Preorder Sequence in Binary Search Tree

Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree. 
You may assume each number in the sequence is unique.
Follow up: Could you do it using only constant space complexity?
Example:
      5
     / \
    2   6
   / \   \
  1   4   7
  
Preorder: 5->2->1->4->6->7
Inorder: 1->2->4->5->6->7 (ascending order)
'''

# lower_bound is the root of left sbutree
# if the current one is greater than the last one in stacks, pop all smaller ancestor values,
# because the current value is larger, then we must now be in their right subtrees, 
# need to maintain the invariant that only left subtree in stack.


import sys
class Solution(object):
    def verifyPreorder(self, preorder):
        """
            :type preorder: List[int]
            :rtype: bool
            """
        lower_bound = -sys.maxint + 1
        stack = []
        for i in range(len(preorder)):
            if preorder[i] < lower_bound:
                return False
                
            while stack and preorder[i] > stack[-1]:
                lower_bound = stack.pop()
            stack.append(preorder[i])

        return True
