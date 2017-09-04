'''
Problem:

给两个array找common elements，一个1M长，一个1K长
'''

'''
Solution:

你可以二分，也可以两个指针互相追赶。。这个情况下，明显是从短的数组里枚举每个数，然后二分长的数组.. (当然一开始要排序)..

排序的话用时间 n=1M, m=1k     nlgn+mlgm, 找用时间mlgN
'''

def commonElememt(n,m):
    # n 1M
    # m 1K
    def find(p,n,start,end):
        while start <= end:
            mid = start + (end-start)/2
            if n[mid] == p:
                return True
            elif n[mid] > p:
                end = mid-1
            else:
                start = mid+1
        return False



    n.sort()    # nlgn
    m.sort()    # mlgm
    result = []
    for p in m:
        if find(p, n, 0, len(n)-1):
            result.append(p)
    return result



n = [1,3,5,7,9,10,11,12,13,14,15,16,17,18,19,20]
m = [2,4,6,8,20]
print commonElememt(n,m)
