'''
Problem: Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:
1 -> A
2 -> B
3 -> C
...
26 -> Z
27 -> AA
28 -> AB
'''


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ''
        while n > 0:
            res = chr((n-1)%26 + ord('A')) + res   # 1-based
            n = (n-1)/26
        return res
        
  
  
'''
Problem: Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28
'''



class Solution(object):
    def titleToNumber(self, s):

        num = 0

        for i in range (0,len(s)):
            bit = ord(s[i])-ord('A')+1   # convert char to int
            num *= 26
            num += bit

        return num
