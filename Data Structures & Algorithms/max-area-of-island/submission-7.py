class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        #returns area of island at (r,c)
        def dfs(r,c):
            visited.add((r,c))
            res = 0
            
            if r+1 in range(ROWS) and (r+1,c) not in visited and grid[r+1][c]==1:
                res+=dfs(r+1,c)
            if r-1 in range(ROWS) and (r-1,c) not in visited and grid[r-1][c]==1:
               res+=dfs(r-1,c)
            if c+1 in range(COLS) and (r,c+1) not in visited and grid[r][c+1]==1:
                res+=dfs(r,c+1)
            if c-1 in range(COLS) and (r,c-1) not in visited and grid[r][c-1]==1:
                res+=dfs(r,c-1)
            res+=1
            return res
    
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c]==1:
                    res = max(res,dfs(r,c))
        return res