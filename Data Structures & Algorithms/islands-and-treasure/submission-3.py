class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()



        #bfs and keep filling UNVISITED land cell with iteration of the bfs (whole layer of queue at a time)
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    q.append((r,c))
        
        res = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited or grid[r][c]==-1:
                    continue
                if grid[r][c]==0:  
                    q.append((r+1,c))
                    q.append((r-1,c))
                    q.append((r,c-1))
                    q.append((r,c+1)) 
                else:
                    grid[r][c]=res
                    visited.add((r,c))
                    q.append((r+1,c))
                    q.append((r-1,c))
                    q.append((r,c-1))
                    q.append((r,c+1))

            res+=1

