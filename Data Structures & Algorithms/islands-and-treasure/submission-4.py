class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # start layer by layer bfs at the treasures

        visited = set()
        ROWS= len(grid)
        COLS = len(grid[0])

        q = deque()
        
        # gets all the treasure chests into the queue
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append((r,c))
        count = 0
        
        while q:
            for i in range(len(q)):
                (x,y) = q.popleft()
                if grid[x][y]==2147483647:
                    grid[x][y]=count
                
                visited.add((x,y))
                
                if x+1 in range(ROWS) and grid[x+1][y]==2147483647 and (x+1, y) not in visited:
                    q.append((x+1,y))
                if x-1 in range(ROWS) and grid[x-1][y]==2147483647 and (x-1, y) not in visited:
                    q.append((x-1,y))
                if y+1 in range(COLS) and grid[x][y+1]==2147483647 and (x, y+1) not in visited:
                    q.append((x,y+1))
                if y-1 in range(COLS) and grid[x][y-1]==2147483647 and (x, y-1) not in visited:
                    q.append((x,y-1))
            count+=1