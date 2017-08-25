'''
Problem:

Given a series Intervals [startTime, stopTime). Find a timestamps that appear most times in the interval.

e.g. [1,3), [2, 7), [4, 8), [5, 9)
5, 6 appears 3 times, so return 5,6.

'''


def findMaxOverLapTime(intervals):
    if not intervals: return []

    points = []
    for interval in intervals:
        points.append([interval[0], 's'])
        points.append([interval[1], 'e'])
    points.sort()

    maxInterval = 0
    nIntervals = 0
    start = end = 0

    for p in points:
        if p[1] == 's':
            nIntervals += 1
            if nIntervals > maxInterval:
                maxInterval = nIntervals
                start = p[0]
        else:
            if nIntervals == maxInterval:
                end = p[0]
            nIntervals -= 1

    result = []
    for i in range(start, end):
        result.append(i)
    return result


intervals = [[1,3],[2,7],[4,8],[5,9]]
print findMaxOverLapTime(intervals)
