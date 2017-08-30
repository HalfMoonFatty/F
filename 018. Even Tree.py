'''
Problem:

You are given a tree (a simple connected graph with no cycles). The tree has N nodes numbered from 1 to N.

Find the maximum number of edges you can remove from the tree to get a forest such that each connected component of the forest
contains an even number of vertices.

# http://www.allprogrammingtutorials.com/tutorials/even-tree-challenge.php
'''

'''
Solution:

Each child's subtree is also a subtree of this node, so the child subtree edge removals 
counts towards this node's edge removal count.

Since we are interested in even-sized forest, and we want to maximize the number of removed edges, 
the problem is equivalent to find the most number of even-sized forests. 
This can be done with a greedy approach, i.e. as soon as we discovered a forest with even size, we cut it off its parent.

p.s. Greedy proof is by contradiction. Suppose the optimal solution contains a forest F1 that contains this current small forest F2. 
We know both F1 and F2are even sized. We can then remove F2 from F1, ending up with 2 even-sizedforests, still each with even size. 
This contradicts the optimal solution.
'''




class Node(object):
  def __init__(self, id):
    self._id = id
    self._children = []

  def AddChild(self, node):
    self._children.append(node)

  def AddChildren(self, nodes):
    self._children.extend(nodes)

  def GetChildren(self):
    return self._children

def DecomposeEvenForest(node):
  count = 0  # number of nodes in the subtree rooted at node.
  edges_to_remove = 0  # Numbeer of edges removed so far across the subtree.

  for child in node.GetChildren():
    sub_count, sub_edges_to_remove = DecomposeEvenForest(child)

    edges_to_remove += sub_edges_to_remove

    if sub_count % 2 == 0:  # if can cut between me and my child so I don't care
      edges_to_remove += 1
    else:   # otherwise keep the connection between me and my child and accumulate my child's node to me(root)
      count += sub_count

  count += 1  # Include the node itself in count.
  return count, edges_to_remove





# Test cases. See link on top of this file for picture.
nodes = [Node(i) for i in range(11)]  # nodes[0] is unused.
nodes[1].AddChildren([nodes[3], nodes[6], nodes[2]])
nodes[3].AddChild(nodes[4])
nodes[6].AddChild(nodes[8])
nodes[2].AddChildren([nodes[7], nodes[5]])
nodes[8].AddChildren([nodes[9], nodes[10]])
assert DecomposeEvenForest(nodes[1])[1] == 2
