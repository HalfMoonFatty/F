'''
Problem:

Find least number of intervals from A that can fully cover B

For example:
Given A=[[0,3],[3,4],[4,6],[2,7]] B=[0,6] return 2 since we can use [0,3] [2,7] to cover the B
Given A=[[0,3],[4,7]] B=[0,6] return 0 since we cannot find any interval combination from A to cover the B

'''


'''
Solution:

Time complexity: O(nlgn)
'''

from operator import itemgetter,attrgetter

class interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def toString(self):
        return "start is:  " + str(self.start) + " end is: " + str(self.end)



def findCover(intervals, interval):

    intervals.sort(key=attrgetter('start'))

    count = 0
    start, end = interval.start, -1
    i = 0 
    while i < len(intervals) and end < interval.end:
        if intervals[i].end <= start:    # 太短了没什么用
            i += 1
            continue
        if intervals[i].start > start:   # 跟前一个end连不上
            break
        while i < len(intervals) and end < interval.end and intervals[i].start <= start:
            end = max(intervals[i].end, end)
            i += 1

        if start != end:
            count += 1
            start = end


    if end < interval.end:
        return 0

    return count


i1 = interval(0,3)
i2 = interval(3,4)
i3 = interval(4,6)
i4 = interval(2,7)
i = interval(0,6)
intervals = [i1,i2,i3,i4]

print findCover(intervals, i)

