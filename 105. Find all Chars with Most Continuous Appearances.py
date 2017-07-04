'''
Problem:

Example： “this send meet” -> [s, e] 再比如：“this is pea” ->[t,h,i,s,i,s,p,e,a] 这个题他只给出input和output让猜程序是干什么的。

Tricky part: 注意skip空格

'''

# Solution: 先扫一遍，统计一下连续字符个数，然后再扫，添加结果

def mostContinuous(s):
    result = []
    if not s or not len(s.strip()): return result

    s = s.replace(" ", "")

    dp = [0]*len(s)
    dp[0] = 1
    maxLen = 1

    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
        maxLen = max(maxLen,dp[i])

    print dp
    for i in range(len(dp)):
        if dp[i] == maxLen:
            result.append(s[i])

    return result


t1 = "this send meet"
t2 = "this is pea"
print mostContinuous(t1)
print mostContinuous(t2)
