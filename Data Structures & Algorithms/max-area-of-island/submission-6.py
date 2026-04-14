class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #output: max area of an island in the grid


        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()


        #returns area of the island at (r,c)
        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited or grid[r][c]==0:
                return 0
            

            visited.add((r,c))
            
            return 1+dfs(r+1,c)+dfs(r-1,c)+dfs(r,c-1)+dfs(r,c+1)


        maxarea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c]!=0:
                    area = dfs(r,c)
                    maxarea = max(maxarea, area)
        return maxarea


        