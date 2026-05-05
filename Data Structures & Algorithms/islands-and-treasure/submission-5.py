class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # layer by layer BFS

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()

        queue = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==0:
                    queue.append((r,c))
        
        iter = 0
        while queue:
            for i in range(len(queue)):
                curr_r,curr_c = queue.popleft()
                if grid[curr_r][curr_c] == 2147483647:
                    grid[curr_r][curr_c] = iter
                visited.add((curr_r,curr_c))

                if curr_r+1 in range(ROWS) and (curr_r+1,curr_c) not in visited and grid[curr_r+1][curr_c]!=-1:
                    queue.append((curr_r+1,curr_c))
                if curr_r-1 in range(ROWS) and (curr_r-1,curr_c) not in visited and grid[curr_r-1][curr_c]!=-1:
                    queue.append((curr_r-1,curr_c))
                if curr_c+1 in range(COLS) and (curr_r,curr_c+1) not in visited and grid[curr_r][curr_c+1]!=-1:
                    queue.append((curr_r,curr_c+1))
                if curr_c-1 in range(COLS) and (curr_r,curr_c-1) not in visited and grid[curr_r][curr_c-1]!=-1:
                    queue.append((curr_r,curr_c-1))
            iter+=1
        