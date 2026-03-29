class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        visit = set() #why set?
        islands = 0 #return value

        def bfs(r,c): #bfs is iterative algo
            q = collections.deque()
            visit.add((r,c))
            q.append((r,c))

            while q:
                row, col = q.popleft()
                if row+1 in range(rows) and grid[row+1][col] == "1" and (row+1,col) not in visit:
                    q.append((row+1,col))
                    visit.add((row+1,col))
                if row-1 in range(rows) and grid[row-1][col] == "1" and (row-1,col) not in visit:
                    q.append((row-1,col))
                    visit.add((row-1,col))
                if col-1 in range(cols) and grid[row][col-1] == "1" and (row,col-1) not in visit:
                    q.append((row,col-1))
                    visit.add((row,col-1))
                if col+1 in range(cols) and grid[row][col+1] == "1" and (row,col+1) not in visit:
                    q.append((row,col+1))
                    visit.add((row,col+1))
                        


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c) #form island (visit the 1s attached to this 1)
                    islands+=1
        return islands
        