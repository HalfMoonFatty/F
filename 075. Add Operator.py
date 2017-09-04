'''
Problem: 

You have a string of numbers, i.e. 123. You can insert a + or - sign in front of ever number, or you can leave it empty. 
Find all of the different possibilities, make the calculation and return the sum. 

For example; 
+1+2+3 = 6 
+12+3 = 15 
+123 = 123 
+1+23 = 24 
... 
-1-2-3 = 6 
... 
Return the sum of all the results.

'''

def addOperator(number):

    def helper(number, index, res, result):
        if index == len(number):
            result.add(eval(res[:]))
            return

        for i in range(index, len(number)):
            if i != index and number[index] == '0':    # note: leading '0'
                return
            num = number[index:i+1]
            helper(number, i+1, res + "+" + num, result)
            helper(number, i+1, res + "-" + num, result)

    result = set()
    helper(number, 0, '', result)
    return list(result)

print addOperator('103')  




'''
Problem:

给你一个数字由1-9组成，给你一个target value，可以在数字中间加 + 或者 -, 问你有多少种组合可以得到target value。
同时有一个eval method，把表达式传进去，返回计算结果。

写完后，让跑test,最后问时间复杂度。
'''



import collections
def findTargetSumWays(nums, S):

    dp = [collections.defaultdict(int) for _ in range(len(nums)+1)]
    dp[0][0] = 1
    
    for i in range(1,len(nums)+1):
        for j in range(1,i+1):
            for k in dp[i-j].keys():
                dp[i][k+nums[i-j]] += dp[i-j][k]
                dp[i][k-nums[i-j]] += dp[i-j][k]

    return dp[-1][S]
