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

# Solution 1 -- Print Nested LinkedList

def flattenPrint(head):
     if not head: return
     while head:
          print head.val
          if head.branch:
               flattenPrint(head.branch)
          head = head.next
          



# Solution 2 --   Flatten Nested LinkedList

def flattenNestedLinkedList(head):

    def helper(cur, prev):
      
        prev.next = cur
        itr = prev
        
        # flatten branch
        while cur:
            print cur.val
            if cur.branch:
                next = cur.next
                tail = helper(cur.branch, cur)
                tail.next = next
                itr = tail
                cur = next 
            else:
                itr = itr.next
                cur = cur.next

        return itr # tail of the branch



    if not head: return None
    dummyhead = ListNode(0)
    helper(head,dummyhead)
    return head 


