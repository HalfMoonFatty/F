'''
Problem:

找小偷问题，有n个房间, 其中一个房间有小偷。早上我们可以打开一个房间的门看小偷在不在里面，晚上小偷会向左边或者右边的房间走。

现在给你一个sequence, 你输出这个sequence能不能保证找到小偷。

比如如果这有三个房间那么如果打开房间的sequence是{1，1}，就一定会找到小偷。因为如果小偷在中间那第一天就会被找到。如果小偷在两边那第二天一定回来到中间也会被找到。

房间数为n, sequence 长度为k。
'''

# Time: O(m*n)
# Space: O(n)

def findTheaf(rooms, strategy):

    found = [False] * rooms
    found[strategy[0]] = True

    for day in range(1, len(strategy)):
        lastDay = found[:]
        for room in range(rooms):
            if room == 0:
                found[room] = lastDay[room+1]
            elif room == rooms-1:
                found[room] = lastDay[room-1]
            else:
                found[room] = lastDay[room-1] or lastDay[room+1]
        found[strategy[day]] = True

    result = True
    for i in range(rooms):
        result = result and found[i]
    return result



rooms = 8
strategy = [1,1]
print findTheaf(rooms, strategy)
