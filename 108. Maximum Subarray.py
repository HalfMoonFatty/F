'''
Problem:

Find the subarray within an array (containing at least TWO number) which has the largest sum. 
For example, given the array [-2,-1,-3,-4,-1], the contiguous subarray [-2,-1] has the largest sum = -3. 
try to do it in O(n) time 

Followup, if input is stream, how to solve it 
public int maxSubArray(int[] nums) {}
'''

class Solution:

    def continuousSubarraySum(self, A):

        maxSum, curSum = -sys.maxint-1, 0
        start = 0
        ret = [0,0]
        
        for i in range(len(A)):
            if curSum >= 0:
                curSum += A[i]
            else:
                curSum = A[i]
                start = i
                
            # both cases can update maxSum, allneg case
            if curSum > maxSum:
                maxSum = curSum
                ret = [start,i]

        return ret
