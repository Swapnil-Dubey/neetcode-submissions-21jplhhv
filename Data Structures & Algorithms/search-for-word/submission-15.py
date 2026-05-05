class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking problem
        # start searching for word (dfs call) on word[0] in the board
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(n,r,c):
            if n == len(word):
                return True
            if word[n]==board[r][c]:
                res = False
                visited.add((r,c))
                #search around for next
                if (r+1)>=0 and (r+1)<=ROWS-1 and (r+1,c) not in visited:
                    res = res or dfs(n+1,r+1,c)
                if (r-1)>=0 and (r-1)<=ROWS - 1 and (r-1,c) not in visited:
                    res = res or dfs(n+1,r-1,c)
                if (c+1)>=0 and (c+1)<=COLS-1 and (r,c+1) not in visited:
                    res = res or dfs(n+1,r,c+1)
                if (c-1)>=0 and (c-1)<=COLS-1 and (r,c-1) not in visited:
                    res = res or dfs(n+1,r,c-1)

                visited.remove((r,c))
                if n == len(word)-1:
                    return True
                return res
            else:
                return False





        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]==word[0]:
                    res = dfs(0,r,c) 
                    if res == True:
                        return True
        return False
