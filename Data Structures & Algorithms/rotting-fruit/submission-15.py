class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #start bfs at rotten fruit, layer by layer extend until u cant anymore(queue is empty)

        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        numfresh=0
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    numfresh+=1
        
        
        res = 0
        while q:
            orig = numfresh

            for i in range(len(q)):
                r,c = q.popleft()
                if r not in range(ROWS) or c not in range(COLS) or (r,c) in visited or grid[r][c]==0:
                    continue


                visited.add((r,c))
                


                if r+1 in range(ROWS) and c in range(COLS) and grid[r+1][c]==1:
                    grid[r+1][c] = 2
                    numfresh-=1
                    q.append((r+1,c))
                if r-1 in range(ROWS) and c in range(COLS) and grid[r-1][c]==1:
                    grid[r-1][c] = 2
                    numfresh-=1
                    q.append((r-1,c))
                if r in range(ROWS) and c-1 in range(COLS) and grid[r][c-1]==1:
                    grid[r][c-1] = 2
                    numfresh-=1
                    q.append((r,c-1))
                if r in range(ROWS) and c+1 in range(COLS) and grid[r][c+1]==1:
                    grid[r][c+1] = 2
                    numfresh-=1
                    q.append((r,c+1))

                
            #TIME ONLY PASSES IF SOMETHING ACTUALLY SPREADS: use numfresh for that
            if numfresh!=orig:
                res+=1

            
        

        if numfresh>0:
            return -1
        else:
            return res