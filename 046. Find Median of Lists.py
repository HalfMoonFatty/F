'''
Problem:

Given list of sorted integer arrays, find the median of all numbers. 

e.g. [1,3,6,7,9], [2,4,8], [5], return 5
'''

'''
Solution:

Use a min Head which is priorityQueue to pop out the minimum number
each time pop one, counter plus one util counter equals to the totalNumber / 2
Time complexity: O(nlgK) -- lgk for sort in the priotiyqueue and pop out n /2 times, space complexity: O(k)
'''

import heapq

def findMedian(nums):
    heap = []
    total = 0
    
    for i in range(len(nums)):
        heapq.heappush(heap, [nums[i][0],i,0])
        total += len(nums[i])

    median, previous = 0.0, 0.0
    count = 0
    while count <= total/2:
        val, i, index = heapq.heappop(heap)
        count += 1
        previous, median = median, val
        if index < len(nums[i])-1:
            heapq.heappush(heap,[nums[i][index+1], i, index+1])
    if total % 2 == 0:
        return (previous + median) / 2.0
    return median


test = [[1,3,6,7,9], [2,4,8], [5]]
print findMedian(test)
