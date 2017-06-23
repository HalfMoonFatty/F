'''
Problem: Find longest arithmetic subsequence in an unsorted array.
'''

'''
Solution:

The idea is to maintain a 2d array. Called length[input.length][input.length]
length[i][j] means the length of the arithmetic that ends with input[i] and input[j]

And a hashMap to record the index of every number.

Traverse the input from index 1 to the end.

Everytime we meet a number, fix this as the end of sequence

Then traverse back and try to make every number as second last number

When we fix one as second last one number, we calculate the "gap" as input[last] - input[secondLast]

look into hashmap to find if there a number in the input equals to "input[secondLast] - gap".

And check from the back of the index[nextVal] to see whether it is smaller than secondLast.

If it is. Then this is the third last number. And we should already have length[thridLast][secondLast]

Then length[secondLast][last] = length[thridLast][secondLast] + 1

If it is not. We make length[secondLast][last] = 2 -- those two number are the only numbers in the arithmetic

Time complexity: O(n^2), space complexity: O(n^2) -- for only return length
'''

import collections
def LongestArithmeticSequence(nums):
    if len(nums) <= 2: return len(nums)

    n = len(nums)
    maxLen = 2
    length = [[0] * (n + 1) for _ in range(n+1)]
    
    # build up index lookup table
    index = collections.defaultdict(list)
    for i in range(n):
        index[nums[i]].append(i)

    # iterate through the array and fix i as the last elem 
    for i in range(1,n):
        # j iterate from i to 0
        for j in range(i-1,-1,-1):
            gap = nums[i] - nums[j]
            nextVal = nums[j] - gap
            # check if there a number in the input equals to "input[secondLast] - gap"
            if index.has_key(nextVal):
                k = -1
                # check from the back of the index[nextVal] to see whether it is smaller than j
                for _ in range(len(index[nextVal])-1, -1, -1):   # check from the back of the index list 
                    if index[nextVal][_] < j:
                        k = index[nextVal][_]
                        break
                if k != -1:
                    length[j][i] = length[k][j] + 1
                    maxLen = max(maxLen, length[j][i])

            if length[j][i] == 0: 
                length[j][i] = 2


    return maxLen

test = [5,4,2,6,6,-1,-2,6,-4,6,-4]
print LongestArithmeticSequence(test)
return 4



# Follow-up: print out the sequence
# Time complexity: O(n^2), space complexity: O(n^2 * m) --m is the average length of all the arithmetic sequence'


import collections
def LongestArithmeticSequence(nums):
    if len(nums) <= 2: return nums

    n = len(nums)
    maxLen = 2
    length = [[None] * (n + 1) for _ in range(n+1)]
    result = []

    # build up index lookup table
    index = collections.defaultdict(list)
    for i in range(n):
        index[nums[i]].append(i)

    for i in range(1,n):
        for j in range(i-1,-1,-1):
            gap = nums[i] - nums[j]
            nextVal = nums[j] - gap
            if index.has_key(nextVal):
                k = -1
                for _ in range(len(index[nextVal])-1, -1, -1):
                    if index[nextVal][_] < j:
                        k = index[nextVal][_]
                        break
                if k != -1:
                    length[j][i] = length[k][j][:] + [nums[i]]
                    if maxLen <= len(length[j][i]):
                        result = length[j][i]
                        maxLen = max(maxLen, len(length[j][i]))


            if not length[j][i]: 
                length[j][i] = [nums[j], nums[i]]


    return result

test = [5,4,2,6,6,-1,-2,6,-4,6,-4]
print LongestArithmeticSequence(test)
return [5, 2, -1, -4]


