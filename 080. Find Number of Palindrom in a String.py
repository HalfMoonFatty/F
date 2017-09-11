'''
Problem 1:

Given a string, the task is to count all palindrome substring in a given string. 

Length of palindrome substring is greater then or equal to 2.

Examples:
Input : str = "abaab"
Output: 3
Explanation : All palindrome substring are : "aba" , "aa" , "baab" 

Input : str = "abbaeae"
Output: 4
Explanation : All palindrome substring are : "bb" , "abba" ,"aea","eae"
'''

def countPS(s):

    n = len(s)
    isPal = [[False] * (n+1) for _ in range(n+1)]
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(i-1,-1,-1):
            if s[j-1] == s[i-1] and (i-j<=2 or isPal[j+1][i-1]):
                isPal[j][i] = True
            if isPal[j][i]: 
                dp[j][i] = dp[j][i-1] + dp[j+1][i] - dp[j+1][i-1] + 1
            else:
                dp[j][i] = dp[j][i-1] + dp[j+1][i] - dp[j+1][i-1]
    return dp[0][n-1]



print countPS("abaab")
print countPS("abbaeae")




'''
Problem 2: Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

'''
Solution:

Calculate and maintain 2 DP states:

- pal[i][j] , which is whether s[i..j] forms a pal
- minCuts[i], which is the minCut for s[i..n-1]; minCuts[0] initially sets to -1, which is needed in the case that s[0..i-1] is a palindrome.
if s[i..j] is a palindrome, then minCuts[j+1] will be updated to the minimum of the current minCuts[j+1] and minCut[i]+1
(i.e. cut s[0..j] into s[0,i-1] and s[i,j]).

Time:  O(N^2)
Space: O(N^2)
'''

class Solution(object):
    def minCut(self, s):
        """
            :type s: str
            :rtype: int
            """
        n = len(s)
        isPal = [[False] * n for _ in range(n)]
        minCuts = [0]*(n+1)
        for i in range(n+1): minCuts[i] = i-1

        for i in range(1,n+1):
            for j in range(i-1,-1,-1):
                if s[j] == s[i-1] and (i-1-j<2 or isPal[j+1][i-2]):
                    isPal[j][i-1] = True
                    minCuts[i] = min(minCuts[i], 1 + minCuts[j])

        return minCuts[-1]
        
        
