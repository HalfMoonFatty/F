'''
Problem:

Check if a tree is a subtree of another tree.

'''

# Time complexity: O(nk) -k nodes in subtree

def isValid(root1, root2):

    def helper(root1, root2):
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (root1 and not root2):
            return False
        if root1.val == root2.val:
            return helper(root1.right, root2.right) && helper(root1.left, root2.left)
        return False

        

    if not root1 and not root2:
        return True

    result = False
    if root1 and root2:
        if root1.val == root2.val:
            result = helper(root1, root2)
        if not result:
            result = isValid(root1.right, root2)
        if not result:
            result = isValid(root1.left, root2)
    return result

