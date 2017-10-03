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







// Quick select to find K points(find Kth smallest element)
public static List<Point> quickFindPoints(int K, Point center, Point[] points) {
    quickSelect(K, points, center, 0, points.length - 1);
    List<Point> rs = new ArrayList<>();
    for (int i = 0; i < K; i++) {
        rs.add(points[i]);
    }
    return rs;
}

public static void quickSelect(int K, Point[] points, Point center, int start, int end) {
    Random rd = new Random();
    int pivot = rd.nextInt(end - start + 1) + start; 
    int i = start;
    int j = end - 1;
    double distance = getDistance(points[pivot], center);
    swap(points, pivot, end);
    while (i < j) {
        while (i < j && getDistance(points[i], center) <= distance) {
            i++;
        }
        while (i < j && getDistance(points[j], center) > distance) {
            j--;
        }
        swap(points, i, j);
    }
    swap(points, end, i);
    int amount = i - start + 1;
    if (K > amount) {
        quickSelect(K - amount, points, center, i + 1, end);
    } else if (K < amount) {
        quickSelect(K, points, center, start, i - 1);
    } else {
        return;
    }
}

public static void swap(Point[] points, int i, int j) {
    Point temp = points[i];
    points[i] = points[j];
    points[j] = temp;
}

public static double getDistance(Point A, Point B) {
    int xDistance = Math.abs(A.x - B.x);
    int yDistance = Math.abs(A.y - B.y);
    return Math.sqrt(Math.pow(xDistance, 2) + Math.pow(yDistance, 2));
}
	
