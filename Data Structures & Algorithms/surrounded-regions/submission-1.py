class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #trick for this one is that run dfs from edge 
        #cells that are Os , all the cells u reach are 
        #not surrounded. rest of them are.
        grid = board
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()


        def dfs(r,c):
            visited.add((r,c))

            if (r+1) in range(ROWS) and (r+1, c) not in visited and grid[r+1][c]=='O':
                dfs(r+1,c)
            if (r-1) in range(ROWS) and (r-1, c) not in visited and grid[r-1][c]=='O':
                dfs(r-1,c)
            

            if (c-1) in range(COLS) and (r, c-1) not in visited and grid[r][c-1]=='O':
                dfs(r,c-1)
            if (c+1) in range(COLS) and (r, c+1) not in visited and grid[r][c+1]=='O':
                dfs(r,c+1)

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c==0 or c==COLS-1) and grid[r][c]=="O":
                    dfs(r,c)


        
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c]=='O':
                    grid[r][c]='X'
                
                



