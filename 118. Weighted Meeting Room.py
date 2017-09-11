'''
Problem:

Given a series of meetings, how to schedule them. Cannot attend more than a meeting at the same time. 
Goal is to find maximum weight subset of mutually non-overlap meetings.

class Meeting:
def __init__(self):
    self.startTime
    self.endTime
    self.weight

# http://www.geeksforgeeks.org/weighted-job-scheduling/
'''


# Common helpers shared by both recursion and dp solutions.

class Job(object):
  def __init__(self, start, finish, profit):
    self.start = start
    self.finish = finish
    self.profit = profit

def latestNonConflict(jobs, i):
  j = i - 1
  while j >= 0:
    if jobs[j].finish <= jobs[i].start:
      return j
    j -= 1
  return -1


# Recursion solution.

def findMaxProfitRec(jobs):
  if len(jobs) == 1:
    return jobs[0].profit

  # Find profit when current job is included.
  inclProf = jobs[-1].profit
  i = latestNonConflict(jobs, len(jobs)-1)
  if i != -1:
    inclProf += findMaxProfitRec(jobs[:i+1])

  # Find profit when current job is excluded.
  exclProf = findMaxProfitRec(jobs[:len(jobs) - 1])

  return max(inclProf, exclProf)

def findMaxProfitWithRecursion(jobs):
  sorted(jobs, key=lambda elem: elem.finish)
  return findMaxProfitRec(jobs)




# DP solution.

def findMaxProfitWithDp(jobs):
  sorted(jobs, key=lambda elem: elem.finish)
  dp = [0] * len(jobs)
  dp[0] = jobs[0].profit

  for i in range(len(jobs)):
    profit = jobs[i].profit
    j = latestNonConflict(jobs, i)
    if j != -1:
      profit += dp[j]
    dp[i] = max(dp[i - 1], profit)

  return dp[-1]


jobs = [
  Job(3, 10, 20),
  Job(1, 2, 50),
  Job(6, 19, 100),
  Job(2, 100, 200),
]

print findMaxProfitWithRecursion(jobs)
print findMaxProfitWithDp(jobs)
