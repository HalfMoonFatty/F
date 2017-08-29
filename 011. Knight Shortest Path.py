'''
Problem:

一个骑士在一个无限大的有障碍的国际象棋棋盘. calculate the shortest path to some target.

Follow-up: how to optimize: A*, pruning.
Edge case: how to end the program? what kinds of target is unreachable and how to avoid?      
'''

# Solution 1: return the shorstest distance

def shortestPath(start, end, blocks):
    xDir = [0,1,0,-1]
    yDir = [1,0,-1,0]

    step = 0
    visited = set()
    visited.add(start)
    q = collections.deque()
    q.append(start)

    while len(q):
        step += 1
        for i in range(len(q)):
            x,y = q.popleft()
            for d in range(4):
                nx, ny = x+xDir[d], y+yDir[d]
                if nx, ny == end:
                    return step
                if [nx,ny] not in visited and [nx,ny] not in blocks:
                    q.append([nx,ny])
                    visited.add([nx,ny])
    return -1



# Solution 2: return the shorstest path

def findPath(start, end, blocks):
    xDir = [0,1,0,-1]
    yDir = [1,0,-1,0]

    found = False
    path = []
    previous = {}    # change visited(set) to lookuptable(dict)
    previous[start] = None
    q = collections.deque()
    q.append(start)
    
    while len(q) and not found:
        x,y = q.popleft()
        for d in range(4):
            nx, ny = x+xDir[d], y+yDir[d]
            if (nx,ny) not in previous and (nx,ny) not in blocks:
                q.append((nx,ny))
                previous[(nx,ny)] = (x,y)
            if (nx,ny) == end:
                found = True

    mover = end
    while mover:
        path.append(previous[mover])
        mover = previous[mover]

    return path
    




# Solution 3: 

public int knightPath(Point2 start, Point2 end, Set<Point2> blocks) {
        int[][] nextStep = {{1, -2}, {1, 2}, {-1, 2}, {1, -2}, {2,-1}, {2, 1}, {-2, -1}, {-2, 1}};
        Queue<Point2> explore = new LinkedList<>();
        Set<Point2> visited = new HashSet<>();
        int step = 0;
        explore.offer(start);
        visited.add(start);
        while (!explore.isEmpty()) {
            step++;
            int size = explore.size();
            for (int i = 0; i < size; i++) {
                Point2 point = explore.poll();
                for (int k = 0; k < 8; k++) {
                    int x = nextStep[k][0];
                    int y = nextStep[k][1];
                    int nextX = point.x + x;
                    int nextY = point.y + y;
                    Point2 next = new Point2(nextX, nextY);
                    boolean canReach1 = true;
                    boolean canReach2 = true;
                    if (Math.abs(y) > Math.abs(x)) {
                        int tempY = y;
                        while (Math.abs(tempY) > 0) {
                            Point2 check = new Point2(point.x, point.y
                            Point2 check2 = new Point2(nextX, point.y
                            canReach1 = blocks.contains(check) ?
                            canReach2 = blocks.contains(check2) ?
                            tempY = tempY > 0 ? tempY - 1 : tempY + 1;
                        }
                    }
                    else {
                        int tempX = x;
                        while (Math.abs(tempX) > 0) {
                            Point2 check = new Point2(point.x + tempX,
                            Point2 check2 = new Point2(point.x + tempX
                            canReach1 = blocks.contains(check) ?
                            canReach2 = blocks.contains(check2) ?
                            tempX = tempX > 0 ? tempX - 1 : tempX + 1;
                        }
                    }
                    if ((!canReach1 && !canReach2) || blocks.contains(next)) { 
                        continue; 
                    }
                    if (next.equals(end)) {
                        return step;
                    }
                    if (!visited.contains(next)) {
                        explore.add(next);
                        visited.add(next);
                    }
                  }
                }
              }
              return -1; 
            }
          }
