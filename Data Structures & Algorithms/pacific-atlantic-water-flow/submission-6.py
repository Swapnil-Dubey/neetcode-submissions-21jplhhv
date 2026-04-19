class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #dfs at all the cells at r==0 and col==0 to form a set of cells visitable 
        #by pacific ocean, do the same for atlantic ocean

        ROWS = len(heights)
        COLS = len(heights[0])

        visitedbypacific = set()
        visitedbyatlantic = set()

        def dfs(x,y,visited):
            visited.add((x,y))

            if x+1 in range(ROWS) and heights[x+1][y]>=heights[x][y] and (x+1,y) not in visited:
                dfs(x+1,y,visited)
            if x-1 in range(ROWS) and heights[x-1][y]>=heights[x][y] and (x-1,y) not in visited:
                dfs(x-1,y,visited)
            if y+1 in range(COLS) and heights[x][y+1]>=heights[x][y] and (x,y+1) not in visited:
                dfs(x,y+1,visited)
            if y-1 in range(COLS) and heights[x][y-1]>=heights[x][y] and (x,y-1) not in visited:
                dfs(x,y-1,visited)


        for r in range(ROWS):
            for c in range(COLS):
                if r == 0 or c==0:
                    dfs(r,c, visitedbypacific)
                if r == ROWS-1 or c == COLS-1:
                    dfs(r,c,visitedbyatlantic)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visitedbypacific and (r,c) in visitedbyatlantic:
                    res.append((r,c))
        
        return res

        