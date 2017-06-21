'''
Problem:

Remove target char from source string. Move the target char to the end of the source string.

'''

'''
Solution:

Traverse the string and put the non-target character into the char array one by one, and put the target character at the end.

'''


def moveChar(s, target):
    s = list(s)
    j = 0
    for i in range(len(s)):
        if s[i] != target:
            s[j], s[i] = s[i], s[j]
            j += 1
    return ''.join(s)


s = 'abbcdbbbbbbb'
target = 'b'
print moveChar(s, target)



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
