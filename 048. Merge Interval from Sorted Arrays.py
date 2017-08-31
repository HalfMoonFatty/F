'''
Problem:

'''

'''
Solution:

Use minHeap to poll out the interval with smallest start time

Check if it has next interval to push into heap in its list

Then check heap.peek(), which has the smallest start time
check if heap.peek().start <= curInterval.end then we need to merge. poll out this interval and merge
curInterval.end = Math.max(curInterval.end, heap.peek().end)

Keep doing the operation above util heap.peek().start > curInterval.end
Add curInterval to result.

Time complexity: O(nlgk) -- k lists of interval, total number of interval is n
Space complexity: O(k) -- space of min heap
'''

import heapq

def mergeSortedIntervals(intervals):

    if not intervals: return []

    result = []
    heap = []
    for i in range(len(intervals)):
        if len(intervals[i]): heapq.heappush(heap,[intervals[i][0].start,i,0])  # start, list index, elem index

            
    while len(heap):
        cur_starttime, cur_Index, cur_i = heapq.heappop(heap)
        heapq.heappush(heap, [intervals[cur_Index][cur_i+1].start, cur_Index, cur_i+1])
        # merge
        while len(heap) and intervals[cur_Index][cur_i].end >= heap[0][0]:
            next_starttime, next_Index, next_i = heapq.heappop(heap)
            intervals[cur_Index].end = max(intervals[cur_Index].end, intervals[next_Index].end)
            if next_i+1 < len(intervals[next_Index]): heapq.heappush(heap, [intervals[next_Index][next_i], next_Index, next_i+1)
        result.append(intervals[cur_Index])

    return result
