'''
Problem:

  *             *           *
 / \           / \         / \ 
1   *   and   *   0   =   *   0
   / \       / \         / \
  0   1     1   0       1   0


Follow up1: deepCopy(tree)
Follow up2: 如何合并结果中出现的情况？

  *
 / \  =>  0
0   0

'''

def andBinaryTree(root1, root2):
    def isLeaf(root):
        return not root.left and not root.right

    def copyTree(root):
        if not root: return None
        copyRoot = TreeNode(root.val)
        copyRoot.left = copyTree(root.left)
        copyTree.right = copyTree(root.right)
        return copyRoot

    def handleAnd(leaf, root):
        if leaf.val == 0: 
            return TreeNode(0)
        else:
            return copyTree(root)


    if isLeaf(root1) and not isLeaf(root2):
        return handleAnd(root1, root2)
    elif isLeaf(root2) and not isLeaf(root1):
        return handleAnd(root2, root1)
    elif isLeaf(root1) and isLeaf(root2):
        if root1.val == 0 or root2.val == 0:
            return TreeNode(0)
        return TreeNode(1)

    root = TreeNode(*)
    root.left = andBinaryTree(root1.left, root2.left)
    root.right = andBinaryTree(root1.right, root2.right)
    return root
