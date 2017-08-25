'''
Problem:

n houses, k colors. neighboring houses cannot be painted with the same color.

NOTE: neighboring relationship is given by adjacent list which means a house may have multiple neighbors.
'''

# Python program for solution of M Coloring 
# problem using backtracking
 
import collections
class Graph(object):
 
    def __init__(self, n, pairs):
        self.graph = collections.defaultdict(list)
        for pair in pairs:
            self.graph[pair[0]].append(pair[1])
            self.graph[pair[1]].append(pair[0])
        self.n = n


    def canColored(self, m):

        def paintHouse(house):
            def isSafe(house, c):
                for n in self.graph[house]:
                    if colors[n] == c:
                        return False
                return True

            if house == self.n:
                return True
            for c in range(m):
                if isSafe(house, c):
                    colors[house] = c
                    if paintHouse(house+1):
                        return True
                    colors[house] = -1
            return False

        colors = [-1] * self.n
        return paintHouse(0)


        

g = Graph(4, [[0,1],[0,2],[0,3],[1,2],[2,3]])
print "Yes" if g.canColored(3) else "No"
