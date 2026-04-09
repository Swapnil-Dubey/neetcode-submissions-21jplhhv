class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #input = grid
        #output = max area of islands
        #constraints: 1 <= grid.length, grid[i].length <= 50
        # pattern: graphs
        #approach:
        #time complexity:
        #space complexity: 

        ROWS= len(grid)
        COLS = len(grid[0])
        visited = set()

        def area(x,y):
            #returns area of the island starting at (x,y)
            if x not in range(ROWS) or y not in range(COLS) or grid[x][y]==0 or (x,y) in visited:
                return 0
            
            visited.add((x,y))
            ret = 1+area(x+1,y)+area(x-1,y)+area(x,y+1)+area(x,y-1)
            return ret
        

        res = 0
        for x in range(ROWS):
            for y in range(COLS):
                res = max(res, area(x,y))
        return res