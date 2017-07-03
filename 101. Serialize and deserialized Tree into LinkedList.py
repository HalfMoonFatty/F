'''
Problem:

Serialize and deserialized Tree into LinkedList
'''

class SerDesTree(object):

    def __init__(self):
        self.itr = None

        
    def serialize(root):

        def serHelper(root):
            if not root: 
                return [ListNode("#"),ListNode("#")]   # [head, tail]
            
            head = tail = ListNode(str(root.val))

            left = serHelper(root.left)
            tail.next = left.head
            tail = left.tail

            right = serHelper(root.right)
            tail.next = right.head
            tail = right.tail

            return [head, tail]

        return serHelper(root)[0]    # [head, tail]
    


    def deserialize(head):
        def desHelper():
            self.itr = self.itr.next
            if self.itr.val == "#":
                return None
            root = TreeNode(int(self.itr.val))
            root.left = desHelper()
            root.right = desHelper()
            return root


        dummyhead = ListNode("")
        dummyhead.next = head
        self.itr = dummyhead
        return desHelper()
