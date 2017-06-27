'''
Problem:

给定一个array 返回一个partition point可以返回该index左边的和和右边的和一样，没有就返回-1，这个要求时间空间最优

Given an array of integers greater than zero, find if it is possible to split it in two (without reordering the elements), 
such that the sum of the two resulting arrays is the same. Print the resulting arrays.

'''

# Time: O(n)
# Space: O(1)

def partitionArray(nums):
    sums = sum(nums)
    rightSum = 0
    for i in range(len(nums)-1,-1,-1):
        sums -= nums[i]
        rightSum += nums[i]
        if rightSum == sums:
            return i
    return -1

test = [1,2,3]
print partitionArray(test)
