class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #output = int mins (min number of mins before all fruits are rotten)
        #constrains: 1 <= grid.length, grid[i].length <= 10
        #pattern: graphs
        #edge cases: fresh fruit is far apart/no fresh fruits (how to check we are done?)
        #approach: BFS ( layer by layer of the queue, starting at rotten fruits)
        #time complexity: 
        #space complexity: 
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        fresh= 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))


        while q and fresh>0:
            for i in range(len(q)): # this just takes snapshot of the original queue even though we are  adding to the q as we iterate on it
                r,c = q.popleft()
                if (r+1) in range(ROWS) and (r+1,c) not in q and grid[r+1][c]==1:
                    q.append((r+1,c))
                    grid[r+1][c]=2
                    fresh-=1
                if (r-1) in range(ROWS) and (r-1,c) not in q and grid[r-1][c]==1:
                    q.append((r-1,c))
                    grid[r-1][c]=2
                    fresh-=1
                if (c+1) in range(COLS) and (r,c+1) not in q and grid[r][c+1]==1:
                    q.append((r,c+1))
                    grid[r][c+1]=2
                    fresh-=1
                if (c-1) in range(COLS) and (r,c-1) not in q and grid[r][c-1]==1:
                    q.append((r,c-1))
                    grid[r][c-1]=2
                    fresh-=1
            time+=1
        if fresh==0:
            return time 
        else:
            return -1


                 



            





