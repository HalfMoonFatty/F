'''
Problem:
    Implement strStr().
    Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

'''
Solution: No need to use "KMP" algorithm. Brute Force with 2 pointers is already good enough.
'''

class Solution(object):
    def strStr(self, haystack, needle):

        if not needle:
            return 0
            
        m = len(haystack)
        n = len(needle)
        
        for i in range(m-n+1):
            j = 0
            while j < n and haystack[i + j] == needle[j]:   
                j += 1
                
            if j == n:
                return i
        return -1

    
    
'''
Follow-up: Strstr 2d Array

把第一个haystack参数变成一个二维数组，然后找needle在haystack第一次出现的位置，同样的不能用string相关方法.
还是返回把haystack[][]二维数组看成一维以后的第一次匹配的字符下标，
Example: haystack := [[a,b,c,c], [c,b,d]], needle := [c,c,b,d] , return 2; needle := [b, d] return 5 (5是把haystack看成一维以后的找到第一个bd以后b的下标)
'''


def strStr2D(haystack, needle):
    total = 0
    for row in range(len(haystack)):
        for col in range(len(haystack[0])):
            i, j, k = row, col, 0
            while i < len(haystack) and j < len(haystack[0]) and k < len(needle) \
            and haystack[i][j] == needle[k]:
                k += 1
                j += 1
                if j == len(haystack[0]):
                    i += 1
                    j = 0
                    
            if k == len(needle):
                return total + j - 1

        total += len(haystack[0])

    return -1

