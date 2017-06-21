'''
Problem:

Reconstruct BST From Pre-order Sequence.
'''


# Solution 1: Recursive

def constructBST(preorder):

    def constructHelper(preorder, start, end):
        root = TreeNode(preorder[start])
        if start == end: return root

        # find the index of the right Tree
        start += 1
        rightIndex = start
        while rightIndex < end and preorder[rightIndex] < root.val:
            rightIndex += 1

        left, right = None, None
        if rightIndex > start: left = constructHelper(preorder, start, rightIndex-1)
        if rightIndex <= end: right = constructHelper(preorder, rightIndex, end)
        root.left = left
        root right = right 
        return root

    if not preorder: return None
    return constructHelper(preorder, 0, len(preorder)-1)
    
    
    
    
# Solution 2: Iterative

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):

        if not root: return ''
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        ans = str(root.val)
        if left: ans += ',' + left
        if right: ans += ',' + right
        return ans



    def deserialize(self, data):
    
        if not data: return None
        nstack, rstack = [], [0x7FFFFFFF]
        for val in map(int, data.split(',')):
            node = TreeNode(val)
            if nstack:
                if val < nstack[-1].val:
                    nstack[-1].left = node
                    rstack.append(nstack[-1].val)
                else:
                    while val > rstack[-1]:
                        while nstack[-1].val > nstack[-2].val:
                            nstack.pop()
                        rstack.pop()
                        nstack.pop()
                    nstack[-1].right = node
            nstack.append(node)
        return nstack[0]
