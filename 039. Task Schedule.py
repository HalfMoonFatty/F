'''
Problem:

Task那道题，很多面经都提到过。就是比如给你一串task，再给一个cooldown，执行每个task需要时间1，两个相同task之间必须至少相距cooldown的时间，问执行所有task总共需要多少时间。
比如执行如下task：12323，假设cooldown是3。总共需要的时间应该是 1 2 3 _ _ 2 3，也就是7个单位的时间。再比如 1242353，假设cool down是4，那总共时间就是 
1 2 4 _ _ _ 2 3 5 _ _ _ 3，也就是13个单位的时间基于1，给出最优的排列，使得字符串最短。


# Tasks: 1, 1, 2, 1
# Recovery interva (cooldown): 2
# Output: 7  (order is 1 _ _ 1 2 _ 1)

# Example 2
# Tasks: 1, 2, 3, 1, 2, 3
# Recovery interval (cooldown): 3
# Output: 7  (order is 1 2 3 _ 1 2 3). more info on 1point3acres.com

# Example 3
# Tasks: 1, 2, 3 ,4, 5, 6, 2, 4, 6, 1, 2, 4. 1point3acres.com/bbs
# Recovery interval (cooldown): 6
# Output: 18  (1 2 3 4 5 6 _ _ 2 _ 4 _ 6 1 _ 2 _ 4)
*/
'''


def taskSchedule(tasks, cooldown):
    result = ''
    index_map = {}
    for t in tasks:
        while index_map.has_key(t) and index_map[t] + cooldown > len(result):
            result += '_'

        result += str(t)
        index_map[t] = len(result)

    return result


t1 = [1, 1, 2, 1]
k1 = 2
print taskSchedule(t1, k1)

t2 = [1, 2, 3, 1, 2, 3]
k2 = 3
print taskSchedule(t2, k2)

t3 = [1, 2, 3 ,4, 5, 6, 2, 4, 6, 1, 2, 4]
k3 = 6
print taskSchedule(t3, k3)


# Follow-up: 
# 1. 求出给定task的工作总时间. O(n)
# 2. How to schedule the tasks to have min total work time
# Solution 2: 一旦时间最多的task cooldown时间到了就schedule这个task.

