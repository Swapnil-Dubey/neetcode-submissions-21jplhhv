class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #run dfs at every position in the grid (try to form island), then run dfs at adjacent positions of the positoin u are are on
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        res = 0

        def dfs(row, col):
            if not (row in range(ROWS) and col in range(COLS)) or (row,col) in visited or grid[row][col] != "1":
                return
            
            # we have to make sure increment only once per island (since we call dfs on every position of the board, we can do it then for the positions we have not visited)
            visited.add((row,col))
            dfs(row+1,col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row,col-1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    res+=1
                    dfs(r,c)
        return res
        
            
            





