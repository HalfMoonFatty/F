'''
Problem: Convert binary tree to double linked list

'''

          1
       //    \\
     2         3
   // \\     // \\
  4     5   6     7



          1
         | |  
     2   | |   3
   // \\ | | // \\
  4     5   6     7
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
