'''
Problem:

Given a sorted array of integers: [-3, -1, 0, 1, 2]. Generate a sorted array of their squares: [0, 1, 1, 4, 9]

'''

# Time: O(n)

def sortArraySquares(nums):
    if not nums: return []

    result = []
    i,j = 0, len(nums)-1
    while i <= j:
        if abs(nums[i]) < abs(nums[j]):
            result.append(nums[j]*nums[j])
            j -= 1
        else:
            result.append(nums[i]*nums[i])
            i += 1
    return result[::-1]



n = [-3, -1, 0, 1, 2]
print sortArraySquares(n)
