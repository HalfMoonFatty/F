'''
Problem: Convert binary tree to double linked list

'''

          4
       //    \\
     2         6
   // \\     // \\
  1     3   5     7



          4
         | |  
     2   | |   6
   // \\ | | // \\
  1     3   5     7           1-2-3-4-5-6-7-(1)
 ||_______________||
 ||---------------||
   
   



# Time complexity O(nlgn)

def BTtoLikedList(root):
    
    def connect(root):
        if not root: return

        if root.left:
            left = root.left
            connect(left)    # recursion
            while left.right:
                left = left.right
            left.right = root
            root.left = left

        if root.right:
            right = root.right
            connect(right)    # recursion
            while right.left:
                right = right.left
            right.left = root
            root.right = right




    if not root: return None

    connect(root)    # recursion

    head, tail = root, root
    while head.left:
        head = head.left
    while tail.right:
        tail = tail.right
    head.left = tail
    tail.right = head

    return head




'''
Follow - up: Revert double linked list back to BST

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
'''


class Solution(object):
    def sortedListToBST(self, head):
        """
            :type head: ListNode
            :rtype: TreeNode
            """

        start = head
        # note: 2 base cases
        if not start: return None
        if not start.next: return TreeNode(start.val)    

        # use fast and slow poiters to find the mid point
        slow, fast = start, start
        prev = ListNode(-10000)     # dummy node
        prev.next = start
        while fast and fast.next:
            fast = fast.next.next   
            slow = slow.next        # slow reaches mid
            prev = prev.next

        # start->...->prev-> mid(slow) ->start2->...->None
        # Break the list into 2 lists
        prev.next = None
        start2 = slow.next

        root = TreeNode(slow.val)    
        root.left = self.sortedListToBST(start)
        root.right = self.sortedListToBST(start2)
        
    return root
