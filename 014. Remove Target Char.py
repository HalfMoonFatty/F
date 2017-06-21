'''
Problem:

Remove target char from source string. Move the target char to the end of the source string.

'''

'''
Solution:

Traverse the string and put the non-target character into the char array one by one, and put the target character at the end.

'''

def removeChar(s, target):
    s = list(s)
    slow = fast = 0
    while fast < len(s):
        # skip first several valid chars
        while slow < len(s) and s[slow] != target:
            slow += 1

        fast = slow
        while fast < len(s) and s[fast] == target:
            fast += 1

        while fast < len(s) and s[fast] != target:
            s[slow] = s[fast]
            s[fast] = target    # set fast to target 
            slow += 1
            fast += 1


    return ''.join(s[:slow])

s = 'abbcdbbafsjo'
target = 'b'
print removeChar(s, target)



'''
Problem:

    Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
    You must do this in-place without making a copy of the array.
    Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        zInd = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zInd], nums[i] = nums[i], nums[zInd]
                zInd += 1
        return
