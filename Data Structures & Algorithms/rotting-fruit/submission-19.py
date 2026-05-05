class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # layer by layer BFS
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        q = deque()
        freshfruits = 0


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c]==1:
                    freshfruits+=1

        
        minute = 0
        while q and freshfruits:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c]=2

                visited.add((r,c))

                if r+1 in range(ROWS) and (r+1,c) not in visited and grid[r+1][c]==1:
                    q.append((r+1,c))
                    grid[r+1][c]=2 # mark rotten when enqueing and decrement freshfruits
                    freshfruits-=1
                if r-1 in range(ROWS) and (r-1,c) not in visited and grid[r-1][c]==1:
                    q.append((r-1,c))
                    grid[r-1][c]=2
                    freshfruits-=1
                if c+1 in range(COLS) and (r,c+1) not in visited and grid[r][c+1]==1:
                    q.append((r,c+1))
                    grid[r][c+1]=2
                    freshfruits-=1
                if c-1 in range(COLS) and (r,c-1) not in visited and grid[r][c-1]==1:
                    q.append((r,c-1))
                    grid[r][c-1]=2
                    freshfruits-=1
        
            minute += 1
        if freshfruits>0:
            return -1
        return minute

