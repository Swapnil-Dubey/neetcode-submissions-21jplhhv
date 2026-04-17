class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #ans is gonna be originating at row 0, last row, col 0, last col
        #   and the ans is gonna be path from one of these originating cells to the other ocean
        grid = heights

        ROWS= len(grid)
        COLS = len(grid[0])

        visitedbypacific = set()
        visitedbyatlantic = set()

        def dfsbypacific(r,c):
            visitedbypacific.add((r,c))

            if r+1 in range(ROWS) and (r+1,c) not in visitedbypacific and grid[r+1][c]>=grid[r][c]:
                dfsbypacific(r+1,c)
            if r-1 in range(ROWS) and (r-1,c) not in visitedbypacific and grid[r-1][c]>=grid[r][c]:
                dfsbypacific(r-1,c)
            if c-1 in range(COLS) and (r,c-1) not in visitedbypacific and grid[r][c-1]>=grid[r][c]:
                dfsbypacific(r,c-1)
            if c+1 in range(COLS) and (r,c+1) not in visitedbypacific and grid[r][c+1]>=grid[r][c]:
                dfsbypacific(r,c+1)
        
        def dfsbyatlantic(r,c):
            visitedbyatlantic.add((r,c))

            if r+1 in range(ROWS) and (r+1,c) not in visitedbyatlantic and grid[r+1][c]>=grid[r][c]:
                dfsbyatlantic(r+1,c)
            if r-1 in range(ROWS) and (r-1,c) not in visitedbyatlantic and grid[r-1][c]>=grid[r][c]:
                dfsbyatlantic(r-1,c)
            if c-1 in range(COLS) and (r,c-1) not in visitedbyatlantic and grid[r][c-1]>=grid[r][c]:
                dfsbyatlantic(r,c-1)
            if c+1 in range(COLS) and (r,c+1) not in visitedbyatlantic and grid[r][c+1]>=grid[r][c]:
                dfsbyatlantic(r,c+1)



        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c == 0:
                    dfsbypacific(r,c)
                if r==ROWS-1 or c==COLS-1:
                    dfsbyatlantic(r,c)
    
        

        
            
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visitedbyatlantic and (r,c) in visitedbypacific:
                    res.append((r,c))
        return res
