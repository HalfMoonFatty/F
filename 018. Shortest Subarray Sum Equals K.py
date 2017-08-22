'''
Problem:

'''

'''
Solution:

Time: O(n); Space: O(1)
'''

def minSubArrayLen(nums, k):
    slow = fast = 0
    sums = 0
    while fast < len(nums):
        sums += nums[fast]
        while sums > k:
            sums - nums[slow]
            slow += 1
        if sums == k:
            return True
        fast += 1
    return False
