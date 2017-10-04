'''
Problem 1: Subarray Sum Equals K

Given an array of positive integers and a target total of X, find if there exists a contiguous subarray with sum = X 
e.g. [1, 3, 5, 18] 
X = 8  Output: True 
X = 9  Output: True 
X = 10 Output: False 
X = 40 Output :False
'''

def subArraySum(nums, target):
    dmap = {0:-1}
    total = 0
    for i, n in enumerate(nums):
        total += n
        if total not in dmap: 
            dmap[total] = i
        if dmap.has_key(total - target): 
            return True

    return False



test = [1, 3, 5, 18] 
for n in [8,9,10,40]:
    print subArraySum(test,n)


    
    
'''
Problem 2:

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size 
at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.
Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
Note:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
'''


'''
Solution:
遍历数组nums，求前i项和total；对k取模，记模值为m
利用dmap[m]记录模为m的前i项和的最小下标，初始令dmap[0] = -1
若 i - dmap[m] > 1，则返回True
'''


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        dmap = {0:-1}
        total = 0
        for i, n in enumerate(nums):
            total += n
            m = total % k if k else total
            if m not in dmap: dmap[m] = i
            elif i - dmap[m] > 1: return True
        return False
    


'''
Problem 3: Longest Subarray Sum Equals to K

Given an array nums and a target value k, find the maximum length of a subarray that sums to k. 
If there isn't one, return 0 instead.

Example 1:
    Given nums = [1, -1, 5, -2, 3], k = 3,
    return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
    Given nums = [-2, -1, 2, 1], k = 1,
    return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

Follow Up:
    Can you do it in O(n) time?
'''

class Solution(object):
    def maxSubArrayLen(self, nums, k):

        mp = {}
        sums = 0
        maxLen = 0
        for i in range(len(nums)):
            sums += nums[i]
            if not mp.has_key(sums):
                mp[sums] = i   # mp stores index
                
            if sums == k:
                maxLen = i + 1
            elif mp.has_key(sums - k):
                maxLen = max(maxLen, i-(mp[sums - k]))  # note: NOT i-(mp[sum - k])+1

        return maxLen


    
    
'''
Problem 4: Shortest Subarray Sums eaquals K
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
        while sums > k and slow < fast:
            sums - nums[slow]
            slow += 1
        if sums == k:
            return True
        fast += 1
    return False




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
                    if sum - nums[i] < s:
                        break
                    sum -= nums[i]
                    i += 1  
                minSize = min(minSize, j-i+1)    # update minSize

        return minSize if minSize <= len(nums) else -1


    
    
'''
Problem 5:

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''


'''
利用字典cnt统计前N项和出现的个数

遍历数组nums：
    在cnt中将sums的计数+1
    累加前N项和为sums
    将cnt[sums - k]累加至答案
'''


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = sums = 0
        cnt = collections.Counter()
        for num in nums:
            cnt[sums] += 1
            sums += num
            ans += cnt[sums - k]
        return ans
