'''
Problem:

Flatten Nested Linked List.

     12  22
    /   /
  11  21
 /   /
1 - 2 - 3

1 - 11 - 12 - 2 - 21 - 22 - 3

                  
           tail 12  22
               /   /
              11  21
head         /   /
dummyhead - 1 - 2 - 3
prev    branch next

# head is the iterator
# prev is the previous node of iterator (head)
# branch is the list to be flattened

'''

# Solution:
def flattenPrint(head):
     if not head: return
     while head:
          print head.val
          if head.branch:
               flattenPrint(head.branch)
          head = head.next
          


def flattenNestedLinkedList(head):

    def helper(branch, prev):
      
        prev.next = branch
        itr = prev
        
        # flatten branch
        while branch:
            print branch.val
            # if branch has more branches
            if branch.branch:
                next = branch.next
                tail = helper(branch.branch, branch)
                tail.next = next
                itr = tail
                branch = next 
            # if branch has no more branch
            else:
                itr = itr.next
                branch = branch.next

        return itr # tail of the branch



    if not head: return None
    dummyhead = ListNode(0)
    helper(head,dummyhead)
    return head 



