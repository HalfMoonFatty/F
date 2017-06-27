'''
Problem: 

跟Min Stack类似， 实现一个Queue， 然后O（1）复杂度获得这个Queue里最小的元素。
'''

import collections

class minQueue(object):
    def __init__(self):
        self.q = collections.deque()
        self.minq = collections.deque()


    def push(self, val):
        while len(self.minq) and self.minq[-1] > val:
            self.minq.pop()
        self.q.append(val)
        self.minq.append(val)


    def poll(self):
        ret = self.q.popleft()
        if ret == self.minq[0]:
            self.minq.popleft()
        return ret

    def getMin(self):
        return self.minq[0]


mq = minQueue()
test = [1,3,2,0,4]
for elem in test:
    mq.push(elem)
for _ in range(5):
    print mq.getMin()
    mq.poll()
