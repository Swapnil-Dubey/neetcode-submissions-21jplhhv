class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input = 2d grid [[str]]
        #output = number of islands
        #constraints: 1<=grid.length<=100
        #           grid[i][j] == '1' or '0'
        # approach and pattern: graphs: DFS
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        res = 0

        #explore the island attached to (r,c) and mark all the positions on this island as explored
        def dfs(r,c):
            visited.add((r,c))

            if r+1 in range(ROWS) and (r+1,c) not in visited and grid[r+1][c] == '1':
                dfs(r+1,c)
            if r-1 in range(ROWS) and (r-1,c) not in visited and grid[r-1][c] == '1':
                dfs(r-1,c)
            if c+1 in range(COLS) and (r,c+1) not in visited and grid[r][c+1] == '1':
                dfs(r,c+1)
            if c-1 in range(COLS) and (r,c-1) not in visited and grid[r][c-1] == '1':
                dfs(r,c-1)
            




        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c]=='1':
                    dfs(r,c)
                    res+=1
        return res
        
