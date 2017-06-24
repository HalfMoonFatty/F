'''
Problem:

给一个正数n, 打印出所有相加的组合

例如 10 可以打印出:
1+1+1+...1
1+2+1+...1
9+1
10
'''

# Time complexity: O(k) -- k is the number of sums
# Space complexity: O(k * average Length) k == 2 ^ n'


def addSum(target):
    def helper(index, target, sums, res, result):

        if sums == target:
            result.append(res[:])

        for i in range(index, target+1):
            if sums + i > target:
                return
            helper(i, target, sums+i, res+str(i), result)

        return

    result = []
    helper(1, target, 1, '1', result)
    return result + [str(target)]

target = 10
print addSum(target)



