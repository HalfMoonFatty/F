'''
Problem:

给一个2d matrix，每个里面值要么是1要么是0， 假如出现1，后面的数都是1.
找出最左边是1的列
[[0, 0, 1, 1, 1],
[0, 1, 1, 1, 1],
[0, 0, 1, 1, 1],
[0, 0, 0, 0, 0]]
'''

# 从右上角开找就好吧 碰到1往左走 碰到0 往下走
# Time O(m+n); Space O(1)

def find1Column(matrix):
    i, j = 0, len(matrix[0])-1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == 0:
            i += 1
        elif matrix[i][j] == 1:
            j -= 1

    return j+1 

matrix = [[0, 0, 1, 1, 1],[0, 1, 1, 1, 1],[1, 1, 1, 1, 1],[0, 1, 1, 1, 1]]
print find1Column(matrix)

