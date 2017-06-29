'''
Problem:

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place, do not allocate extra memory.
Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''


'''
Solution: 2 pointers
Step 1. From back to front: find the first index(j) break the trend: nums[i-1] >= nums[i]  前一个比后一个大
Step 2. From back to front: find the smallest number which is larger than nums[j] (the break point)to make sure that we have the RIGHT NEXT permutation
Step 3. Swap nums[j] and nums[i]
Step 4. After swapping, reverse the rest of the array (nums[j+1:])
'''



class Solution(object):
    def nextPermutation(self, nums):

        if not nums:
            return None

        j = 0
        # Find the first index(j) break the trend: nums[i-1] >= nums[i] 应该前一个比后一个大
        for i in range(len(nums)-1, -1, -1):
            if nums[i-1] < nums[i]:
                j = i-1
                break

        # Find the smallest number which is larger than nums[j], the break point
        if j >= 0:
            for i in range(len(nums)-1, j, -1):
                if nums[i] > nums[j]:    # 找到第一个比 nums[j] 大的 nums[i]
                    nums[j], nums[i] = nums[i], nums[j]    # swap position
                    break
        
        # Reverse the rest
        nums[j+1:] = nums[j+1:][::-1]
        return
    
    
    
'''    
Follow - up: Previous Permutation

The idea is that find the last two adjacent number that the first one is beigger than the second one

Then the question come to that find the previous permutation of the nums[first-end]
Then sequence after second must be acending, so the previous permutation must comes from 
the number that is samller than the nums[first] at the position first with a decending sequence after it

e.g. 5, 4, 1, 2, 3 previous -> 5, 3, 4, 2, 1
the num[first] = 4, nums[second] = 1, nums[smaller] = 3
'''

class Solution(object):
    def previousPermutation(self, nums):

        if not nums:
            return None

        j = 0
        # Find the first index(j) break the trend: nums[i-1] <= nums[i] 应该前一个比后一个小
        for i in range(len(nums)-1, -1, -1):
            if nums[i-1] > nums[i]:  # here 
                j = i-1
                break

        # Find the smallest number which is larger than nums[j], the break point
        if j >= 0:
            for i in range(len(nums)-1, j, -1):
                if nums[i] < nums[j]:    # 找到第一个比 nums[j] 小的 nums[i]
                    nums[j], nums[i] = nums[i], nums[j]    # swap position
                    break
        
        # Reverse the rest
        nums[j+1:] = nums[j+1:][::-1]
        return

