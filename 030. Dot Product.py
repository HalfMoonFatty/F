'''
Problem: Dot Product

A={a1, a2, a3,...}
B={b1, b2, b3,...} 
dot_product=a1*b1+a2*b2+a3*b3 +...

1. 如果数组很稀疏，如 A={a1, ...., a300, ...., a5000}.B={...., b100, ..., b300, ..., b1000, ...} 有很多0, 用什么数据结构表示能节省空间？
用 list 存：
A=[[1, a1], [300, a300], [5000, a5000]]
B=[[100, b100], [300, b300], [1000, b1000]]. 

2. Given
A=[[1, a1], [300, a300], [5000, a5000]]
B=[[100, b100], [300, b300], [1000, b1000]]. 
求 dot product. 

3. 时间复杂度。
O(max(len(A),len(B)))

'''

def dotProduct(A, B):
    indexA = indexB = 0
    product = 0
    while indexA < len(A) and indexB < len(B):
        if A[indexA][0] == B[indexB][0]:
            product += A[indexA][1] * B[indexB][1]
            indexA += 1
            indexB += 1
        elif A[indexA][0] > B[indexB][0]:
            indexB += 1
        else:
            indexA += 1
    return product
   
   
   
'''    
Follow-up:
如果length(B) >>> length(A)，即B非常长，怎么做能减少时间复杂度？

对A里面的每个数， binary search找B中相对应的值，
这样时间复杂度是O(nlogm) (n = len(A), m = len(B)).

'''    
    
def dotProduct(A, B):
    def binarySearch(B, index):
        start, end = 0, len(B)-1
        while start <= end:
            mid = start + (end-start)/2
            if B[mid][0] == index:
                return mid
            elif B[mid][0] > index:
                end = mid-1
            else:
                start = mid+1
        return -1

    product = 0
    for indexA, valA in A:
        indexB = binarySearch(B, indexA)
        if indexB != -1:
            product += valA * B[indexB][1]
    return product
