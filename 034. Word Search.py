'''
Problem 1:

Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
For example, Given board =
    [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
    ]
    word = "ABCCED", -> returns true,
    word = "SEE", -> returns true,
    word = "ABCB", -> returns false.
'''


class Solution(object):
    def exist(self, board, word):

        def dfsSearch(index, r, c, visited):
            if index == len(word):
                return True

            if r<0 or r>=len(board) or c<0 or c>=len(board[0]) or visited[r][c]:
                return False
    
            # check current index
            if word[index] != board[r][c]:
                return False
            
            visited[r][c] = True
            dr = (0,1,0,-1)
            dc = (1,0,-1,0)
            for i in range(4):
                if dfsSearch(index+1, r+dr[i], c+dc[i], visited):
                    return True
            visited[r][c] = False


        m = len(board)
        n = len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if dfsSearch(0, i, j, visited):
                    return True
        return False
        
        
        
'''
problem:
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once in a word.
For example, Given words = ["oath","pea","eat","rain"] and
board =
[
['o','a','a','n'],
['e','t','a','e'],
['i','h','k','r'],
['i','f','l','v']
]
Return ["eat","oath"].
Note:
	You may assume that all inputs are consist of lowercase letters a-z.
	You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?
	If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. 
	What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? 
	If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
'''


class Solution(object):
    def findWords(self, board, words):

        def dfsSearch(node, r, c, string, results):
            # boundary or visited
            if r>len(board)-1 or c>len(board[0])-1 or r<0 or c<0 or visited[r][c]:
                return

            # check trie
            cur = board[r][c]
            if not node.children.has_key(cur):
                return
            if node.children[cur].isWord:
                results.add(string+cur)
                
            visited[r][c] = True
            dfsSearch(node.children[cur], r-1, c, string+cur, results)
            dfsSearch(node.children[cur], r+1, c, string+cur, results)
            dfsSearch(node.children[cur], r, c-1, string+cur, results)
            dfsSearch(node.children[cur], r, c+1, string+cur, results)
            visited[r][c] = False
            return


        # build a trie
        trie = Trie()
        for word in words:
            trie.addWord(word)

        results = set()
        visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfsSearch(trie.root, i, j, '', results)
        return list(results)
