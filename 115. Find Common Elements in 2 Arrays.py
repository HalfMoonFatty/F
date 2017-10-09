'''
Problem:

给两个array找common elements，一个1M长，一个1K长
'''

'''
Solution:

你可以二分，也可以两个指针互相追赶。。这个情况下，明显是从短的数组里枚举每个数，然后二分长的数组.. (当然一开始要排序)..

n=1M, m=1k 排序的话用时间nlgn, 找用时间mlgN
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
    result = []
    for p in m:
        if find(p, n, 0, len(n)-1):
            result.append(p)
    return result



n = [1,3,5,7,9,10,11,12,13,14,15,16,17,18,19,20]
m = [2,4,6,8,20]
print commonElememt(n,m)



'''
Solution 2: Sorting + 2 pointers
Time: O(nlogn)
Space: O(m)
'''

class Solution(object):
    def intersection(self, nums1, nums2):
        """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
        nums1.sort()
        nums2.sort()
        ans = []

        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                # 去重
                if len(ans) == 0 or ans[-1] != nums1[i]:
                    ans.append(nums1[i])
                i += 1
                j += 1

        return ans



'''
Solution 3: Sorting + Binary Search
Time: O(nlogm)
Space: O(n)
'''
class Solution(object):
    def intersection(self, nums1, nums2):
        """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: List[int]
            """
        def BSearch(s,e,arr,target):
            if e < s:
                return False

            mid = s + (e-s)/2
            if arr[mid] == target:
                return True
            elif arr[mid] > target:
                return BSearch(s,mid-1,arr,target)
            else:
                return BSearch(mid+1,e,arr,target)


        nums2.sort()    
        ans = Set()

        for n in nums1: 
            if BSearch(0, len(nums2)-1, nums2, n):
                ans.add(n)
        return list(ans)
