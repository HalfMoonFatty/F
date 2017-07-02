'''
Problem:

Given an array A of integers, find the index of values that satisfy A + B =C + D, where A,B,C & D are integers values in the array. 
Find all combinations of quadruples.

'''

# Time complexity: O(n^2)

import collections

def findQuadruples(nums):
    if not nums:
        return []

    sumParis = collections.defaultdict(set)
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            sums = nums[i] + nums[j]
            sumParis[sums].add((i,j))
    result = []
    for s in sumParis.keys():
        index = list(sumParis[s])
        res = []
        for i in range(len(index)-1):
            for j in range(i+1, len(index)):
                p1,p2 = index[i], index[j]
                res.append([nums[p1[0]],nums[p1[1]],nums[p2[0]],nums[p2[1]]])
        if res: result.append(res)
    return result


nums = [1,2,3,4,5,6,7,8,9]
print findQuadruples(nums)
