'''
Problem:

Given: 
a encoded to 1 
b encoded to 2 
.... 
z encoded to 26 

You can translate a number to a string: 
'123' can be translated to 'abc', but also can be translated to 'aw','lc' which gives 3 total translations 
'12' can be translated to 'ab' and 'l' -> 2 translations 

Write a function to get the number of valid combinations from a number like '123123123'
'''


class Solution:

    def numDecodings(self, s):

        def isValid(s):
            return 1 if 9 < int(s) < 27 else 0
        
        # corner case
        if len(s) == 0 or s[0] == '0': return 0 
        if len(s) == 1: return 1 if s[0] != '0' else 0
        
        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0 # note: s[0] != '0'
 
        for i in range(2,len(dp)):
            if s[i-1] != '0': dp[i] = dp[i-1]         # Y可以单独解码的条件是：Y != '0'
            if isValid(s[i-2:i]): dp[i] += dp[i-2]    # XY可以解码的条件是：9<XY<=26
            if dp[i] == 0: return 0 # note: early return
        return dp[-1]
            
            



# Space O(1)

class Solution(object):
    def numDecodings(self, s):

        # helper function
        def valid2dig(char1, char2):
            val = int(char1)*10 + int(char2)
            if 9 < val <= 26:
                return 1
            else:
                return 0

        if len(s) == 0 or s[0] == '0': return 0
        if len(s) == 1: return 1 if s[0] != '0' else 0

        # init
        fn_2 = 1    # dp[0] = 1
        fn_1 = 1 if s[0] != '0' else 0
        fn = 0

        for i in range(1,len(s)):
            if s[i] != '0': fn += fn_1
            if valid2dig(s[i-1], s[i]): fn += fn_2  
            if fn == 0: return 0
            # rotate
            fn_2 = fn_1
            fn_1 = fn
            fn = 0

        return fn_1
