class Solution:
    def numIslands(self,grid:[[str]])->int:
        #normal example:
        #edge case:
        #brute force:
        #optimal:

        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        res = 0


        def visit(r,c):
            visited.add((r,c))

            if 0<=r+1<ROWS and (r+1,c) not in visited and grid[r+1][c]=='1':
                visit(r+1,c)
            if 0<=r-1<ROWS and (r-1,c) not in visited and grid[r-1][c]=='1':
                visit(r-1,c)
            if 0<=c+1<COLS and (r,c+1) not in visited and grid[r][c+1]=='1':
                visit(r,c+1)
            if 0<=c-1<COLS and (r,c-1) not in visited and grid[r][c-1]=='1':
                visit(r,c-1)
        

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c]=="1":
                    visit(r,c)
                    res+=1
        return res

                
                