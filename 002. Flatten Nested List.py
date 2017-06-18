'''
Problem:

'''


'''
Solution 1: With iterator

Time complexity: O(n), space complexity: o(n)
'''

#class NestedInteger(object):
#    def isInteger(self):
#
#    def getInteger(self):
#
#    def getList(self):


class NestedIterator(object):

    def __init__(self, nestedList):
        self.stack = []
        for i in range(len(nestedList)-1,-1,-1):
            self.stack.append(nestedList[i])
        

    def next(self):
        if not self.hasNext():
            return -1
        return self.stack.pop().getInteger()
        

    def hasNext(self):
        while len(self.stack):
            curElem = self.stack[-1]
            if curElem.isInteger():
                return True
            else:
                self.stack.pop()
                curList = curElem.getList()
                for i in range(len(curList)-1,-1,-1):
                    self.stack.append(curList[i])
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


'''
Solution 2: Without iterator

Time complexity: O(n), space complexity: o(n)
'''

def flattenNestedList(nestedList):

    result = []

    if not nestedList:
        return result

    # init stack
    stack = []
    for i in range(len(nestedList)-1,-1,-1):
        stack.append(nestedList[i])

    # iterate through the stack
    while len(stack):
        curElem = stack.pop()
        if curElem.isInteger():
            result.append(curElem.getInteger())
        else:
            for i in range(len(curElem.getList())-1,-1,-1):
                stack.append(curElem.getList()[i])
    return result
