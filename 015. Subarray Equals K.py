'''
Problem 1: 给一个数字array, 有正有负数。给一个数， array中是否存在连续的数字，其和是给定的数。
'''

'''
Solution:

Use hashSet to store the sum, range[i ~ j] = sum[j] - sum[i] = k

Set.contains(sum - k), return true
'''

def SubarrayEqualsK(nums, k):
    sums = set()
    accu = 0 
    for n in nums:
        accu += n
        if accu - k in sums:
            return True
        sums.add(accu)
    return False




'''
Problem 2:

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
Problem 3:

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
