'''
Problem:

Given 2 strings and a value K, return if there exist a common substring in these 2 strings. 

e.g. str1 = "leetcode", str2 = "codyabc" and k = 3. "cod" is the common substring with length 3, return True.

'''


def commonSubStr(str1, str2, k):
    # corner case
    if k <= 1: return True   

    dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            if dp[i][j] >= k:
                return True
    return False

s = "leetcode"
t = "codyabc"
k = 3
print commonSubStr(s, t, k)



'''
Follow-up 1: Longest Common Substring
'''
def commonSubStr(str1, str2):
    
    if k <= 1: return True   
    
    lcs = -1
    dp = [[0] * (len(str2)+1) for _ in range(len(str1)+1)]
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            lcs = max(lcs, dp[i][j])

    return False




'''
Follow-up 2: Longest Common Subsequence

1. dp[i][j] 定义为s1, s2的前i,j个字符串的最长common subsequence. 

2. dp[i][j] 
    当char i == char j， dp[i - 1][j - 1] + 1
    当char i != char j,  dp[i][j - 1], dp[i - 1][j] 里取一个大的（因为最后一个不相同，所以有可能s1的最后一个字符会出现在s2的前部分里，反之亦然。
'''

def lcs(s, t):
    
    m = len(s)
    n = len(t)
    dp = [[0]*(n+1) for i in range(m+1)]
 
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
 
    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return dp[m][n]
 
 
# Driver program to test the above function
s = "AGGTAB"
t = "GXTXAYB"
print "Length of LCS is ", lcs(s, t)
