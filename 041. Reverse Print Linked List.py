'''
Problem:

Iterate over a singly linked list backwards. Call print on each node. 

Example: The list A->B->C should print as 
"C B A"
class Node {
  public Node next;
  public String value;
}

There are 4 solutions 
1) recursive 
2) iterative with O(n) memory (reverse the list)
3) iterative with O(1) memory and O(n2) runtime 
4) iterative with O(1) memory and O(n) runtime (for this solution the initial list may be modified) 
Explain all 4 solutions and write the code for solutions 3 and 4

'''


# 1) Recusive Print Linked List: O(n) Time; O(n) Space

def printReverse(head):
    if not head: return
    printReverse(head.next)
    print(head.val)
        
      
# 2) Using Stack: Iterative with O(n) Time; O(n) Space

def printReverse(head):
    stack = []
    while head:
        stack.append(head.val)
        head = head.next
    while len(stack):
        print stack.pop()

  
# 3) Iterative with O(1) memory and O(n2) runtime 

def printReverse(head):
    last = None
    while head != last:
        curr = head
        while curr.next != last:
            curr = curr.next
        print curr.val
        last = curr
    return
  
  

# 4) Modify the original linkedlist: iterative with O(1) space and O(n) runtime.

def reverseList(head):
    # base case
    if not head or not head.next:
        return head
    
    p = head
    r = None
    while p:
        q = p.next  
        p.next = r
        r = p
        p = q
    return r
 




      

# Reverse Linked List - Recursive 

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # base case
        if not head or not head.next:
            return head
        
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None    # note
        
        return newHead
        
        
        
# Reverse Linked List - Iteratve:

class Solution:

    def reverseList(self, head):
        # base case
        if not head or not head.next:
            return head
        
        p = head
        r = None
        while p:
            q = p.next  
            p.next = r
            r = p
            p = q
        return r
