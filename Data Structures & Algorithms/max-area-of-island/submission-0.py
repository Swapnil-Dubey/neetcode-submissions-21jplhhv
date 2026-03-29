class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visit = set()
        maxarea = 0

        def bfs(row, col):
            nonlocal currarea
            q = collections.deque()
            q.append((row,col))

            while q:
                (r,c) = q.popleft()
                currarea+=1
                if r+1 in range(ROWS) and grid[r+1][c]==1 and (r+1,c) not in visit:
                    q.append((r+1,c))
                    visit.add((r+1,c))
                if r-1 in range(ROWS) and grid[r-1][c]==1 and (r-1,c) not in visit:
                    q.append((r-1,c))
                    visit.add((r-1,c))
                if c+1 in range(COLS) and grid[r][c+1]==1 and (r,c+1) not in visit:
                    q.append((r,c+1))
                    visit.add((r,c+1))
                if c-1 in range(COLS) and grid[r][c-1]==1 and (r,c-1) not in visit:
                    q.append((r,c-1))
                    visit.add((r,c-1))





            
        for r in range(ROWS):
            for c in range(COLS):
                currarea = 0
                if grid[r][c] == 1:
                    visit.add((r,c))
                    bfs(r,c)
                maxarea = max(maxarea, currarea)
        return maxarea
        