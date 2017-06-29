'''
Problem:

Find path from one node to another node in a binary tree node has parent pointer
'''

def findPath(root, node1, node2):
    def findLength(node):
        length = 0
        while node:
            node = node.parent
            length += 1
        return length


    if not node1 or not node2: 
        return []

    result = []
    left, right = [], []
    itr1, itr2 = node1, node2
    length1, length2 = findLength(itr1), findLength(itr2)

    while length1 > length2:
        left.append(itr1.val)
        itr1 = itr1.parent
        length1 -= 1

    while length2 > length1:
        right.append(itr2.val)
        itr2 = itr2.parent
        length2 -= 1        

    while itr1 != itr2:
        left.append(itr1.val)
        right.append(itr2.val)
        itr1 = itr1.parent
        itr2 = itr2.parent
    left.append(itr1.val) # LCA
    
    result.extend(left)
    result.extend(right[::-1])
    return result
