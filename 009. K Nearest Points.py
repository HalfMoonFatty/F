'''
Problem:

给2D平面上的N个点，求离原点最近的K个点

Given some points in two dimensional space, find k points out of all points which are nearest to origin(0,0)
'''

'''
Solution: Use max Heap

maintain a max heap with size K,
every time meet a new point, check if its distance is smaller than the heap[-1]
if yes, pop out the peek, push this point into heap
in the end we will have K points which are the nearest points

Time complexity: O(nlgk), space complexity:O(k)
'''

import heapq

def findNearestKPoints(points, k):
    def getDistance(p):
        return p[0]*p[0]+p[1]*p[1]

    result = []
    maxHeap = []
    for p in points:
        if len(maxHeap) < k:
            heapq.heappush(maxHeap,[-getDistance(p),p])
        elif getDistance(p) < -maxHeap[0][0]:
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap,[-getDistance(p),p])

    while len(maxHeap):
        result.append(heapq.heappop(maxHeap)[1])

    return result


points = [(0,1), (1,0), (1,1), (2,2), (3,3)]
k = 2
print findNearestKPoints(points, k)
