'''
Problem:
Check whether a given graph is Bipartite or not
'''

import collections
class Graph(object):
 
    def __init__(self, n, pairs):
        self.graph = collections.defaultdict(list)
        for pair in pairs:
            self.graph[pair[0]].append(pair[1])
            self.graph[pair[1]].append(pair[0])
        self.n = n
 

    def isBipartite(self, src):
        colors = [-1] * self.n
        colors[src] = 1
        q = collections.deque([src])
        while len(q):
            cur = q.popleft()
            if self.graph.has_key(cur):
                for nei in self.graph[cur]:
                    if self.graph.has_key(nei) and cur in self.graph[nei]: # Note
                        self.graph[nei].remove(cur)
                    if colors[nei] == colors[cur]:
                        return False
                    colors[nei] = 1-colors[cur]
                    q.append(nei)
        return True


g = Graph(4, [[0,1],[0,3],[1,2],[2,3]])
print "Yes" if g.isBipartite(0) else "No"
 
