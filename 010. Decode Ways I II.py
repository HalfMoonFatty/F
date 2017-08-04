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

    
    
'''
Follow-up: Output the result of all decode string

Time complexity: O(1.6 ^ n)
'''

def decode(s):
    def helper(s, i, res, result):
        if i == len(s):
            result.append(res[:])
            return

        # n < 10
        n = int(s[i:i+1])
        if n == 0: return
        helper(s, i+1, res + chr(n+ord('A')-1), result)

        # 9 < n < 26
        if i < len(s)-1:
            n = int(s[i:i+2])
            if 9< n <= 26: 
                helper(s, i+2, res + chr(n+ord('A')-1), result)

        return

    result = []
    helper(s, 0, '', result)
    return result




'''
Problem:
A message containing letters from A-Z is being encoded to numbers using the following mapping way:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from 1 to 9.
Given the encoded message containing digits and the character '*', return the total number of ways to decode it.
Also, since the answer may be very large, you should return the output mod 109 + 7.
Example 1:
Input: "*"
Output: 9
Explanation: The encoded message can be decoded to the string: "A", "B", "C", "D", "E", "F", "G", "H", "I".
Example 2:
Input: "1*"
Output: 9 + 9 = 18
Note:
The length of the input string will fit in range [1, 105].
The input string will only contain the character '*' and digits '0' - '9'.
'''

'''
Complexity Analysis
Time complexity : O(n). dp array of size n+1 is filled once only. Here, n refers to the length of the input string.
Space complexity : O(n). dp array of size n+1 is used.
'''


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        M = 10**9 + 7
        dp = [0]*(len(s)+1)
        dp[0] = 1
        if s[0] == "*": dp[1] = 9
        elif s[0] == "0": dp[1] = 0
        else: dp[1] = 1
        
        for i in range(2, len(dp)):
            if s[i-1] == "*":
                dp[i] = 9*dp[i-1]
                if s[i-2] == "1":
                    dp[i] = (dp[i] + 9*dp[i-2]) % M
                elif s[i-2] == "2":
                    dp[i] = (dp[i] + 6*dp[i-2]) % M
                elif s[i-2] == "*":
                    dp[i] = (dp[i] + 15*dp[i-2]) % M
            else:
                dp[i] = dp[i-1] if s[i-1] != '0' else 0
                if s[i-2] == "1":
                    dp[i] = (dp[i] + dp[i-2]) % M
                elif s[i-2] == "2" and s[i-1] <= '6':
                    dp[i] = (dp[i] + dp[i-2]) % M
                elif s[i-2] == "*":
                    if s[i-1] <= '6':
                        dp[i] = (dp[i] + 2*dp[i-2]) % M
                    else:
                        dp[i] = (dp[i] + dp[i-2]) % M
        return dp[-1]
        
        
        
# Could be further optimiazed to constant space: https://leetcode.com/problems/decode-ways-ii/#/solution
# Time complexity : O(n). dp array of size n+1 is filled once only. Here, n refers to the length of the input string.
# Space complexity : O(1). 
