'''
Problem:

Given an array, generate a tree with the following properties:

1. Binary Tree
2. Min Heap. All children nodes' value are less than root.val
3. Remain the same order when in order traversing the tree.

e.g. [5,2,10,7]

  2 
 / \
5   7
   /
 10

Follow-up:

AddNode(root, val). Keep the origianl properties return root.

'''

'''
Solution:

Find the smallest value in the array and make it as root, left part as left branch, right part as right brandh

Time complexity: O(nlgn), Space complexity: O(lgn)
'''

def BuildMinHeap(nums):
    def helper(nums, start, end):
        if start > end: 
            return None
        val = min(nums[start:end+1])
        root = TreeNode(val)
        root.left = helper(nums, start, end-1)
        root.right = helper(nums, start+1, end)
        return root

    return helper(nums, 0, len(nums)-1)



'''
Solution: 

如果 value > root.val, 就尽量往右放 (maintain inorder traversal order)；
否则就插在 prev 和 itr 之间 (新node在prev右边，itr在新node左边)


Check the root's value, 

if it is bigger than input, we should input it as current node's parent to maintain the inorder traverse order, 
the current node should be the left child of input node

else go into the right child
Time complexity: O(lgn)

[5,2,10,7]

  2 
 / \
5   7
   /
 10


e.g. add 8 => [5,2,10,7,8]

  2 
 / \
5   7
   / \
 10  *8
 

e.g. add 1 => [5,2,10,7,1]

   *1
   /
  2 
 / \
5   7
   /
 10
 

e.g. add 4 => [5,2,10,7,4]

  2 
 / \
5  *4
   /
  7
 /
10

'''


def addOne(root, value):
    itr = root
    prev = None

    while True:
        if value > itr.val:
            if not itr.right:
                itr.right = TreeNode(value)
                break
            prev = itr
            itr = itr.right
        else:
            node = TreeNode(value)
            if prev:
                prev.right = node
            else:
                root = node
            node.left = itr
            break
    return root

