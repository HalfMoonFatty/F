'''
Problem 1:

Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note: You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''


import sys
class Solution(object):
    def shortestDistance(self, words, word1, word2):

        ind1 = -1
        ind2 = -1
        minDis = sys.maxint
        for i,w in enumerate(words):
            # build up index map
            if w == word1:
                ind1 = i
            elif w == word2:
                ind2 = i
            # update the word distance
            if ind1 != -1 and ind2 != -1:
                minDis = min(minDis, abs(ind1 - ind2))
        return minDis
       
       
       
        
'''
Problem 2:

Now you are given the list of words and your method will be called repeatedly many times with different parameters. 
    
How would you optimize it?
Design a class which receives a list of words in the constructor, 
and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list.
    
For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note: You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''


# Solution: Pay attention to index iteration: if index1 < index2, increase index1; else increase index2.

import sys
from collections import defaultdict
class WordDistance(object):
    def __init__(self, words):
        self.indexmp = defaultdict(list)
        for i,w in enumerate(words):
            self.indexmp[w].append(i)


    def shortest(self, word1, word2):
        l1 = self.indexmp[word1]
        l2 = self.indexmp[word2]
        minDis = sys.maxint
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            index1,index2 = l1[i],l2[j]
            if index1 < index2:
                minDis = min(minDis,index2 - index1)
                i += 1
            else:
                minDis = min(minDis,index1 - index2)
                j += 1
        return minDis
        
    
    
    

'''
Problem 3:

This is a follow up of Shortest Word Distance. The only difference is now word1 could be the same as word2.
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
word1 and word2 may be the same and they represent two individual words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.

Note: You may assume word1 and word2 are both in the list.
'''

'''
Solution:
    ind1 and ind2 are the indexes where word1 and word2 were last seen.
    Except if they're the same word, then i1 is the previous index.
'''

import sys
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        ind1 = -1
        ind2 = -1
        minDis = sys.maxint
        for i,w in enumerate(words):
            if w == word1:
                ind1 = i
            # if not elif, so will enter both clause
            if w == word2:
                # if they're the same word,then ind1 is the previous index (ind2).
                if word1 == word2:
                    ind1 = ind2
                ind2 = i    # ind2 is new
            if ind1 != -1 and ind2 != -1:
                minDis = min(minDis, abs(ind1 - ind2))
        return minDis
