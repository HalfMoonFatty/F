'''
Problem:

给一个 partial sorted 的数组，比如 1 3 5 2 4 6 8 10 20 30 11 12  13， 数组有N个数，分为M个segment，N>>>M，要求输出排序后的数组。

time  space  complexity ?

Similar to k sorted list
'''

'''
Solution:

Use a class Number to record the cur number and index and end index of a segment
For instance, we have {1, 3, 9, 2, 6, 8}. Then we have a Number(value = 1, index = 0, endIndex = 2) and Number(value = 2, index = 3, endIndex = 5)

Traverse through the array find the start and end of every segment store the start number of every segment into a min heap.

So every time we use heap, which pop out the samllest number, and we check its index
If the index is samller than the endIndex, which means this segment is not over, we need to put the next number of the segment into heap.

Time complexity: O(nlgm) -n is the number of numbers in array -m is the number of segment
Space complexity: O(n)'
'''

import heapq
def SortPartialSortedArray(nums):
    result = [0] * len(nums)

    heap = []
    start = 0
    for i in range(len(nums)):
        if i > 0 and nums[i] < nums[i-1]:
            heapq.heappush(heap, [nums[start], start, i-1])
            start = i
    heapq.heappush(heap, [nums[start], start, len(nums)-1])

    
    itr = 0
    while len(heap):
        minVal, index, end = heapq.heappop(heap)
        result[itr] = minVal
        itr += 1
        if index < end-1:
            heapq.heappush(heap, [nums[index+1], index+1, end])

    return result


nums = [1,3,5,2,4,6,8,10,20,30,11,12,13]
print SortPartialSortedArray(nums)
