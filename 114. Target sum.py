'''
Problem:

给你一个数字由1-9组成，给你一个target value，可以在数字中间加 + 或者 -, 问你有多少种组合可以得到target value。
同时有一个eval method，把表达式传进去，返回计算结果。
类似于lc282,494的mix。这里和282相比不需要做乘法，并且符号可以加在第一数的前面。
但是和494不同的是数字并不一定是一位，可以是多位组成，这里和282一样。写完后，让跑test,最后问时间复杂度。
'''



import collections
def findTargetSumWays(nums, S):

    dp = [collections.defaultdict(int) for _ in range(len(nums)+1)]
    dp[0][0] = 1
    
    for i in range(1,len(nums)+1):
        for j in range(1,i+1):
            for k in dp[i-j].keys():
                print '\nold dp'
                print i,j,k,dp
                dp[i][k+nums[i-j]] += dp[i-j][k]
                dp[i][k-nums[i-j]] += dp[i-j][k]
                print 'new dp'
                print i,j,k,dp
    return dp[-1][S]




def addOperators(num, target):
    def dfs(res, num, target, curstr, pos, cur_total):
        if pos == len(num) and cur_total == target:    # base case
            res.append(curstr[:])
        else:
            for i in range(pos+1,len(num)+1):
                t = num[pos:i]
                t_val = int(t)
                if str(t_val) != t: continue    # note
                dfs(res, num, target, curstr+"+"+t, i, cur_total+t_val)
                dfs(res, num, target, curstr+"-"+t, i, cur_total-t_val)
        return


    res = []
    if not num:
        return res
    for i in range(1,len(num)+1):
        s = num[:i]
        s_val = int(s)
        if str(s_val) != s: continue
        dfs(res, num, target, s, i, s_val)
        dfs(res, num, target, '-'+s, i, -s_val)
    return res


