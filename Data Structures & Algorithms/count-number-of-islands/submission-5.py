class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input = grid
        #output = number of islands
        # constraints: 1 <= grid.length, grid[i].length <= 100
        #               grid[i][j] is '0' or '1'.
        #pattern = graphs
        #approach:run dfs at every 1 (starting of island) ifff the position is not already visited (bcz every dfs run corresponds to a new island)
        #edge cases:
        #time complexity: O(m*n)^2 
        #space complexity: 

        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(x,y):
            if x not in range(ROWS) or y not in range(COLS) or (x,y) in visited or grid[x][y] == '0':
                return 0
            
            #otherwise its a land that has not been visited
            visited.add((x,y))

            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x,y+1)
            dfs(x,y-1)

            return 1

        res = 0
        for x in range(ROWS):
            for y in range(COLS):
                if (x,y) not in visited:
                    res+= dfs(x,y)
        return res
