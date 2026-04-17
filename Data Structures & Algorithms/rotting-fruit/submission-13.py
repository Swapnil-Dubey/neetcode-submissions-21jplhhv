class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #layer by layer bfs
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])


        q = deque()
        freshfruits = 0

        # add all the rotten fruits to the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                if grid[r][c]==1:
                    freshfruits+=1

        #infect all fruits with bfs layer by layer
        count = 0
        while q and freshfruits:
            for i in range(len(q)):
                (x,y) = q.popleft()
                visited.add((x,y))

                if x+1 in range(ROWS) and grid[x+1][y]==1 and (x+1,y) not in visited:
                    grid[x+1][y] = 2
                    q.append((x+1,y))
                    freshfruits-=1
                if x-1 in range(ROWS) and grid[x-1][y]==1 and (x-1,y) not in visited:
                    grid[x-1][y] = 2
                    q.append((x-1,y))
                    freshfruits-=1
                if y+1 in range(COLS) and grid[x][y+1]==1 and (x,y+1) not in visited:
                    grid[x][y+1] = 2
                    q.append((x,y+1))
                    freshfruits-=1
                if y-1 in range(COLS) and grid[x][y-1]==1 and (x,y-1) not in visited:
                    grid[x][y-1] = 2
                    q.append((x,y-1))
                    freshfruits-=1
            count+=1


        if freshfruits!=0:
            return -1
        else:
            return count
        

