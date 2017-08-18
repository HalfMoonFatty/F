'''
Problem:

给三个funtions: is_low(), is_mid(), is_high(). 让给一个数组排序, low的放在最前面, mid的放在中间, high的放在最后面.

Follow - up: think about when there are K colors

'''

# Solution: one-pass
# Time: O(n)
# Space: O(1)

def sortColors(nums):
    index_low, index_high = 0, len(nums)-1
    index = 0
    while index < index_high and index_low < index_high:
        if is_low(index):
            nums[index_low], nums[index] = nums[index], nums[index_low]
            index_low += 1
            index += 1
        elif is_high(index):
            nums[index], nums[index_high] = nums[index_high], nums[index]
            index_high -= 1
        else:
            index += 1


# Follow - up:

def sortKColors(nums, k):
    left, right = 0, len(nums)-1

    while k > 0:
        # find the minVal and maxVal between left and right
        minVal, maxVal = sys.maxint, -sys.maxint-1
        for i in range(left, right+1):
            minVal = min(minVal, nums[i])
            maxVal = max(maxVal, nums[i])

        # normal 3 way partition
        index = left
        minIndex, maxIndex = left,right
        while minIndex < maxIndex and index < maxIndex:
            if nums[index] == minVal:
                nums[index], nums[minIndex] = nums[minIndex], nums[index]
                index += 1
                minIndex += 1
            elif nums[index] == maxVal:
                nums[index], nums[maxIndex] = nums[maxIndex], nums[index]
                maxIndex -= 1
            else:
                index += 1
                
        # update left, right bound and k
        left, right = minIndex, maxIndex
        k -= 2


 
