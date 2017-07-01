'''
Problem:

Given some rectangles on a plane, return the max overlap rectangle coordinate.

如果给你一堆的矩形， 求重合矩形重合最多的坐标位置。大概思路就是做一个二维的meeting room II

'''



import collections
from collections import OrderedDict

class Rectangle(object):
    def __init__(self, x0, x1, y0, y1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

    def toString(self):
        return str(self.x0) + " , " + str(self.y0) + " , " + str(self.x1) + " , " + str(self.y1)



def findMostOverlap(rectangles):
    indexToLine = collections.defaultdict(list)

    for rec in rectangles:
        indexToLine[rec.x0].append([rec.y0, 'Up', 'Left'])
        indexToLine[rec.x0].append([rec.y1, 'Down', 'Left'])
        indexToLine[rec.x1].append([rec.y0, 'Up', 'Right'])
        indexToLine[rec.x1].append([rec.y1, 'Down', 'Right'])


    for rec in rectangles:
        for index in range(rec.x0+1, rec.x1):
            if indexToLine.has_key(index):
                indexToLine[index].append([rec.y0, 'Up', None])
                indexToLine[index].append([rec.y1, 'Down', None])


    indexToLine = collections.OrderedDict(sorted(indexToLine.items()))   # sort x values from small to large
    for index in indexToLine.keys():
        indexToLine[index].sort(reverse = True)    # sort y values from large to small


    #print indexToLine

    overlap = Rectangle(0,0,0,0)
    maxOverlap = 0
    for index in indexToLine.keys():
        line = indexToLine[index]
        left = right = 0
        for elem in line:
            #print "\ncurrent element is: " + str(index) + str(elem)
            if elem[1] == 'Up':
                if not elem[2] or elem[2] == 'Left':     # Up-Left
                    right += 1
                    if right > maxOverlap:
                        overlap.x0 = index
                        overlap.y0 = elem[0]
                        maxOverlap = right
                if not elem[2] or elem[2] == 'Right':    # Up-Right
                    left += 1

            else:                                        # Down-Right
                if not elem[2] or elem[2] == 'Right':
                    if left == maxOverlap:
                        overlap.x1 = index
                        overlap.y1 = elem[0]
                    left -= 1
                if not elem[2] or elem[2] == 'Left':     # Down-Left
                    right -= 1
            #print "maxOverlap is: " + str(maxOverlap) + ";  left is: " + str(left) + ";  right is: " + str(right) 
            #print overlap.toString()
    return overlap



r1 = Rectangle(0,10,10,0)
r2 = Rectangle(5,15,15,5)
r3 = Rectangle(5,15,15,5)
rectangles = [r1, r2]
print findMostOverlap(rectangles).toString()
