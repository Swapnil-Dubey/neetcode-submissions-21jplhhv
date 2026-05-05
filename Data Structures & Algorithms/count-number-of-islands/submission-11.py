class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #input = grid: [[str]]
        #output = int res: number of islands
        #constraints:
        #edge cases: no islands, all positions in the grid are 1 (1 island)
        # pattern and approach: graph, dfs approach (explore island and mark as visited through a for loop dfs call)
        #time complexity: O(n)
        #space complexity: O(n)


        ROWS = len(grid)
        COLS = len(grid[0]) # imppp remember that COLS is grid[0]
        visited = set()

        #explore all 1's associated with this island
        def dfs(r,c):
            visited.add((r,c))

            if (r+1)>=0 and (r+1)<=ROWS-1 and (r+1,c) not in visited and grid[r+1][c]=='1':
                dfs(r+1,c)
            if (r-1)>=0 and (r-1)<=ROWS-1 and (r-1,c) not in visited and grid[r-1][c]=='1':
                dfs(r-1,c)
            if (c+1)>=0 and (c+1)<=COLS-1 and (r,c+1) not in visited and grid[r][c+1]=='1':
                dfs(r,c+1)
            if (c-1)>=0 and (c-1)<=COLS-1 and (r,c-1) not in visited and grid[r][c-1]=='1':
                dfs(r,c-1)







        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in visited and grid[r][c]=='1': ### imp remember that only explore the unexplored 1's
                    dfs(r,c)
                    res+=1

        return res






