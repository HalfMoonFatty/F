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
