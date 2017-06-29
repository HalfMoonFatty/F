'''
Problem:

Assign independent tasks to n workers. Return the task schedules wuth the shortest time.

'''


# BackTracking

import sys

def taskSchedule(tasks, n):
    def maxTime(schedule):
        maxTime = -1
        time = 0
        for entry in schedule:
            time = sum(entry)
            maxTime = max(maxTime, time)
        return maxTime

    def dfs(tasks, i, n, res, result, minTime):
        if i == len(tasks):
            if maxTime(res) < minTime[0]:
                if result: result.pop()
                result.append([l[:] for l in res])
                minTime[0] = maxTime(res)
                print 'find better: ' 
                print result, minTime
            return

        for j in range(n):     
            res[j].append(tasks[i])
            dfs(tasks, i+1, n, res, result, minTime)
            res[j].pop()


    minTime = [sys.maxint]
    result = []
    res = [[] * len(tasks) for _ in range(n)]
    dfs(tasks, 0, n, res, result, minTime)
    return result

tasks = [2,2,3,7,1]
n = 2
print "final result is: " + str(taskSchedule(tasks,n))



# DP: Backpack problem
