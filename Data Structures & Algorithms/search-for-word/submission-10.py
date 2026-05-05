class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        ROWS = len(board)
        COLS = len(board[0])
        

        def dfs(curr,r,c):
            if board[r][c]!=word[curr]:
                return False
            if curr == len(word)-1:
                return True
            if curr>len(word):
                return False
            

            visited.add((r,c))
            res = False

            if r+1>=0 and r+1<=ROWS-1 and (r+1,c) not in visited:
                res = res or dfs(curr+1,r+1,c)
            if r-1>=0 and r-1<=ROWS-1 and (r-1,c) not in visited:
                res = res or dfs(curr+1,r-1,c)
            if c+1>=0 and c+1<=COLS-1 and (r,c+1) not in visited:
                res = res or dfs(curr+1,r,c+1)
            if c-1>=0 and c-1<=COLS-1 and (r,c-1) not in visited:
                res = res or dfs(curr+1,r,c-1)
            


            visited.remove((r,c))

            return res
            







        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]==word[0]:
                    res = dfs(0, r,c)
                    if res == True:
                        return True
        return False