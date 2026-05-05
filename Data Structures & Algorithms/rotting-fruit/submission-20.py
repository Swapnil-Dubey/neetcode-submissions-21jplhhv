class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        freshfruits= 0

        q = deque()
        minutes =0
       
                




        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    freshfruits+=1
                if grid[r][c]==2:
                    q.append((r,c))
        
        while q and freshfruits:
            for i in range(len(q)):
                r,c = q.popleft()
                visited.add((r,c))

                if (r+1)>=0 and (r+1)<=ROWS-1 and (r+1,c) not in visited and grid[r+1][c]==1:
                    grid[r+1][c]=2
                    freshfruits-=1
                    q.append((r+1,c))
                if (r-1)>=0 and (r-1)<=ROWS-1 and (r-1,c) not in visited and grid[r-1][c]==1:
                    grid[r-1][c]=2
                    freshfruits-=1
                    q.append((r-1,c))
                if (c+1)>=0 and (c+1)<=COLS-1 and (r,c+1) not in visited and grid[r][c+1]==1:
                    grid[r][c+1]=2
                    freshfruits-=1
                    q.append((r,c+1))
                if (c-1)>=0 and (c-1)<=COLS-1 and (r,c-1) not in visited and grid[r][c-1]==1:
                    grid[r][c-1]=2
                    freshfruits-=1
                    q.append((r,c-1))
            minutes+=1
        
        if freshfruits>0:
            return -1
        return minutes