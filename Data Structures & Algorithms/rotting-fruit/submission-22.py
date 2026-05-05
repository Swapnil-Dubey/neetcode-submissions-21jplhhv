class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #input = grid [[int]]
        #output = number of mins in which all oranges rotted
        #constraints: 
        #patterna nd appraoch: layer by layer bfs , mark rotten and then append into queue
        #edge cases: if a fruit is not reachable, 
        # time complexoty
        #space ocmpelxoty


        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        freshfruits = 0
        minutes = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    freshfruits+=1
                if grid[r][c]==2:
                    q.append((r,c))

        while q and freshfruits:
            for i in range(len(q)):
                r,c = q.popleft()
                visited.add((r,c))

                if r+1>=0 and r+1<=ROWS-1 and (r+1,c) not in visited and grid[r+1][c]==1:
                    grid[r+1][c]=2
                    q.append((r+1,c))
                    freshfruits-=1 # remember to decrease freshfruits
                if r-1>=0 and r-1<=ROWS-1 and (r-1,c) not in visited and grid[r-1][c]==1:
                    grid[r-1][c]=2
                    q.append((r-1,c))
                    freshfruits-=1
                if c+1>=0 and c+1<=COLS-1 and (r,c+1) not in visited and grid[r][c+1]==1:
                    grid[r][c+1]=2
                    q.append((r,c+1))
                    freshfruits-=1
                if c-1>=0 and c-1<=COLS-1 and (r,c-1) not in visited and grid[r][c-1]==1:
                    grid[r][c-1]=2
                    q.append((r,c-1))
                    freshfruits-=1
            




            minutes+=1
    


        if freshfruits:
            return -1
        return minutes