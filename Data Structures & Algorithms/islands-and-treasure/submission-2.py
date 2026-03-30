class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #output = grid modified in place with land cells storing dist to nearest treasure chest
        #constraints: m == grid.length
                    # n == grid[i].length
                    # 1 <= m, n <= 100
                    # grid[i][j] is one of {-1, 0, 2147483647}
        #pattern: graphs
        #approach: run bfs starting at every treasure spot
        #time complexity:O(m*n)
        #space complexity: O(m*n)

        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visited = set()
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    queue.append([r,c])
                    visited.add((r,c))
        
        dist = 0
        while queue:
            for i in range(len(queue)): # go through the entire first layer of the queue (gates)
                r,c = queue.popleft()
                grid[r][c] = dist

                if r+1 in range(ROWS) and c in range(COLS) and grid[r+1][c] != -1 and (r+1,c) not in visited:
                    queue.append([r+1,c])
                    visited.add((r+1,c))
                if r-1 in range(ROWS) and c in range(COLS) and grid[r-1][c] != -1 and (r-1,c) not in visited:
                    queue.append([r-1,c])
                    visited.add((r-1,c))
                if r in range(ROWS) and c+1 in range(COLS) and grid[r][c+1] != -1 and (r,c+1) not in visited:
                    queue.append([r,c+1])
                    visited.add((r,c+1))
                if r in range(ROWS) and c-1 in range(COLS) and grid[r][c-1] != -1 and (r,c-1) not in visited:
                    queue.append([r,c-1])
                    visited.add((r,c-1))
            dist+=1
        



        