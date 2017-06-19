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

def flattenNestedLinkedList(head):

    def helper(branch, head):
      
        head.next = branch
        prev = head
        
        # flatten branch
        while branch:
            print branch.val
            # if branch has more branches
            if branch.branch:
                next = branch.next
                tail = helper(branch.branch, branch)
                tail.next = next
                perv = tail
                branch = next 
            # if branch has no more branch
            else:
                prev = prev.next
                branch = branch.next

        return prev # tail of the branch



    if not head: return None
    dummyhead = ListNode(0)
    helper(head,dummyhead)
    return head 



