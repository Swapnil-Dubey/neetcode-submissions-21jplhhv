class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #ans is gonna be originating at row 0, last row, col 0, last col
        #   and the ans is gonna be path from one of these originating cells to the other ocean
        grid = heights

        ROWS= len(grid)
        COLS = len(grid[0])

        visitedbypacific = set()
        visitedbyatlantic = set()

    
        
        def dfs(r,c, visited):
            visited.add((r,c))

            if r+1 in range(ROWS) and (r+1,c) not in visited and grid[r+1][c]>=grid[r][c]:
                dfs(r+1,c, visited)
            if r-1 in range(ROWS) and (r-1,c) not in visited and grid[r-1][c]>=grid[r][c]:
                dfs(r-1,c, visited)
            if c-1 in range(COLS) and (r,c-1) not in visited and grid[r][c-1]>=grid[r][c]:
                dfs(r,c-1, visited)
            if c+1 in range(COLS) and (r,c+1) not in visited and grid[r][c+1]>=grid[r][c]:
                dfs(r,c+1, visited)



        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfs(r,c, visitedbypacific)
                if r==ROWS-1 or c==COLS-1:
                    dfs(r,c, visitedbyatlantic)
    
        

        
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visitedbyatlantic and (r,c) in visitedbypacific:
                    res.append((r,c))
        return res
