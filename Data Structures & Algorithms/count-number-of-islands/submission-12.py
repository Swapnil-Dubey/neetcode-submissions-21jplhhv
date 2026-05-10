class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()



        def dfs(r,c):
            visited.add((r,c))


            if (r+1)>=0 and (r+1)<=ROWS-1 and grid[r+1][c]=='1' and (r+1,c) not in visited:
                dfs(r+1,c)
            if (r-1)>=0 and (r-1)<=ROWS-1 and grid[r-1][c]=='1' and (r-1,c) not in visited:
                dfs(r-1,c)
            if (c+1)>=0 and (c+1)<=COLS-1 and grid[r][c+1]=='1' and (r,c+1) not in visited:
                dfs(r,c+1)
            if (c-1)>=0 and (c-1)<=COLS-1 and grid[r][c-1]=='1' and (r,c-1) not in visited:
                dfs(r,c-1)



        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]=='1' and (r,c) not in visited:
                    dfs(r,c)
                    res+=1
        return res