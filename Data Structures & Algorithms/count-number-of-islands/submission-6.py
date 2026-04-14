class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #return number of islands inthe grid

        #start dfs at every (r,c) that is '1' and not marked visited

        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        

        #forms island starting at (r,c) marks all '1' positions in the island as visited
        def dfs(r,c):
            if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited or grid[r][c]!='1':
                return
            
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            






        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1' and (r,c) not in visited:
                    dfs(r,c)
                    res+=1
        return res