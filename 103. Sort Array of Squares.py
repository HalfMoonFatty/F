'''
Problem:

Given a sorted array of integers: [-3, -1, 0, 1, 2]. Generate a sorted array of their squares: [0, 1, 1, 4, 9]

'''

# Time: O(n)

def sortArraySquares(nums):
    if not nums: return []

    result = [0] * len(nums)
    i,j = 0, len(nums)-1
    k = len(nums)-1
    while i <= j:
        if abs(nums[i]) < abs(nums[j]):
            result[k] = nums[j]*nums[j]
            j -= 1
        else:
            result[k] = nums[i]*nums[i]
            i += 1
        k -= 1
    return result



n = [-3, -1, 0, 1, 2]
print sortArraySquares(n)
