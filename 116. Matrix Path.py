'''
Problem:

Given 2-d matrix with 1s and 0s, where 1 represents obstacle and 0 represents road, find a path from upper left conner to the bottom right conner. 
'''



from collections import deque

def findPath(matrix):
    def dfs(r,c,visited,path,result):
        if result: return

        if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]) or matrix[r][c] == 1 or visited[r][c]:
            return

        if r == len(matrix)-1 and c == len(matrix[0])-1:
            path.append((r,c))
            result.append(path[:])
            return

        xdir, ydir = [1,0,-1,0], [0,1,0,-1]
        for d in range(4):
            visited[r][c] = True
            path.append((r,c))
            dfs(r+xdir[d], c+ydir[d], visited, path, result)
            visited[r][c] = False
            path.pop()
        return

    def bfs(matrix):
        path = []
        previous = {(0,0): None}
        xdir, ydir = [1,0,-1,0], [0,1,0,-1]
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        visited[0][0] == True  
        q = deque()
        q.append([0,0])
        
        while len(q):
            x,y = q.popleft()
            if x == len(matrix)-1 and y == len(matrix[0])-1:
                break   
            for i in range(4):
                nx,ny = x+xdir[i], y+ydir[i]
                if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and not visited[nx][ny] and (nx,ny) not in previous:
                    q.append([nx,ny])
                    visited[nx][ny] = True
                    previous[(nx,ny)] = (x,y)

        mover = (len(matrix)-1, len(matrix[0])-1)
        while mover:
            path.append(mover)
            mover = previous[mover]

        return path
    
 

    #visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]    
    #result = []
    #dfs(0,0, visited, [], result)
    #return result
    return bfs(matrix)


matrix = [[0,0,1,0],[1,0,0,1],[0,1,0,0],[0,0,1,0]]
print findPath(matrix)
