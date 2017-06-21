

def InsertLinkedList(head, node):
    dummyHead = ListNode(0)
    dummyHead.next = head
    prev, itr = dummyHead, head

    while itr and node.val > itr.val:
        itr = itr.next
        prev = prev.next

    prev.next = node
    node.next = itr

    return dummyHead.next
