class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        maxarea = 0
        
        def dfs(row, col): #forms island
            nonlocal currarea
            if row not in range(ROWS) or col not in range(COLS) or grid[row][col]!=1 or (row,col) in visited:
                return
            
            currarea+=1
            visited.add((row,col))

            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col-1)
            dfs(row, col+1)





        for r in range(ROWS):
            for c in range(COLS):
                currarea = 0
                if (r,c) not in visited:
                    dfs(r,c)
                    maxarea = max(maxarea, currarea)

        return maxarea