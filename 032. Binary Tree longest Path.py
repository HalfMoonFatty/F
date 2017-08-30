'''
Problem: Binary Tree longest PATH

'''

def findLongestPath(root):

    def getLongestPath(root):
        
        if not root: return (0,0)    #(depth, longestPath)
        
        left = getLongestPath(root.left)
        right = getLongestPath(root.right)
        across = left[0] + right[0] + 1
        longestPath = max(across, max(left[1], right[1]))    # longestPath = max (across, left.longestPath, right.longestPath)
        depth = max(left[0], right[0])+1     # depth = max(left.depth, right.depth)
        return (depth, longestPath)

    if not root: return 0
    return getLongestPath(root)[1]


