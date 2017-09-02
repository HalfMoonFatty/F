'''
Problem:
    Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. 
    If there isn't one, return 0 instead.
    For example, given the array [2,3,1,2,4,3] and s = 7,
    the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
    If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''


'''
Solution: 快慢指针
Time: O(n)
Space: O(1)
'''

class Solution:

    def minimumSize(self, nums, s):
        if not nums: return -1

        minSize = sys.maxint  
        sum = 0
        i = 0
        for j in range(len(nums)):
            sum += nums[j]
            if sum >= s:
                while i <= j: # try to shrink the current minSize
                    if sum -nums[i]< s:
                        break
                    sum -= nums[i]
                    i += 1  
                minSize = min(minSize, j-i+1)    # update minSize

        return minSize if minSize <= len(nums) else -1

    

    
    
# Follow up: Extend to 2D and find if rectangle sum = k
# Similar Problem: 363. Max Sum of Rectangle No Larger Than K.py

import sys
def sumSubmatrixEqualsK(matrix, k):

    if not matrix: return 0

    res = -sys.maxint-1
    for left in range(0,len(matrix[0])):
        rowSum = [0] * len(matrix)
        for right in range(left, len(matrix[0])):
            sums = {0}
            curSum = 0
            for i in range(len(matrix)):
                rowSum[i] += matrix[i][right]
                curSum += rowSum[i]
                if curSum - k in sums:
                    return True
                sums.add(curSum)

    return False


matrix = [[1,2,3],[4,5,6],[7,8,9]]
k = 27
print sumSubmatrixEqualsK(matrix, k)




'''
Problem:
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a rectangle in the matrix such that its sum is no larger than k.
Example:
Given matrix = [
[1,  0, 1],
[0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).
Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
'''

class Solution(object):
    def maxSumSubmatrix(self, matrix, k):

        if not matrix: return 0

        res = -sys.maxint-1
        for left in range(0,len(matrix[0])):
            rowSum = [0] * len(matrix)
            for right in range(left, len(matrix[0])):
                accuSum = [0]
                curSum,curMax = 0, -sys.maxint -1
                for i in range(len(matrix)):
                    rowSum[i] += matrix[i][right]
                    curSum += rowSum[i]
                    ind = bisect.bisect_left(accuSum,curSum-k)
                    if ind < len(accuSum):
                        curMax = max(curMax,curSum-accuSum[ind])
                    # early return
                    #if curMax == k: return k
                    bisect.insort(accuSum,curSum)

                res = max(res, curMax)

        return res
