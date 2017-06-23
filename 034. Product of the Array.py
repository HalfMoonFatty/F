'''
Problem:

Given an array, return all products of its elements. 

Example: Given array:[1,2,3,4], return [1, 2, 3, 4, 6, 8, 12, 24]
'''


# Solution: Just Like find the subset of the array
# Time complexity: O(2^n)--number of subsets
# Space complexity: O(Len(input))


def arrayProduct(nums):
    def helper(nums, index, res, result, first):
        if not first:
            result.add(res)

        first = False
        for i in range(index, len(nums)): # note i in range(index, len(nums))
            if nums[i] == 0:
                result.add(0)

            if i == index or nums[i] != nums[i-1]:  # note: remove dup
                res *= nums[i]
                helper(nums, i+1, res, result, first)
                res /= nums[i]
        return

    nums.sort()
    result = set()
    helper(nums, 0, 1, result, True)
    return result

test = [1,2,3,4] 
print arrayProduct(test)



