class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #run dfs at first letter of word=
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        res = False


        def dfs(i,r,c):
            nonlocal res
            if i>len(word)-1:
                res = True
                return

            visited.add((r,c))


            if (r+1)>=0 and (r+1)<=ROWS-1 and (r+1,c) not in visited and board[r+1][c]==word[i]:
                dfs(i+1,r+1,c)                                                     
            if (r-1)>=0 and (r-1)<=ROWS-1 and (r-1,c) not in visited and board[r-1][c]==word[i]:
                dfs(i+1,r-1,c)
            if (c+1)>=0 and (c+1)<=COLS-1 and (r,c+1) not in visited and board[r][c+1]==word[i]:
                dfs(i+1,r,c+1)
            if (c-1)>=0 and (c-1)<=COLS-1 and (r,c-1) not in visited and board[r][c-1]==word[i]:
                dfs(i+1,r,c-1)
            
            visited.remove((r,c))                                                               # remember we need to backtrack*

            


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]==word[0]:
                    dfs(1,r,c)
                    if res == True:
                        return True
        return False


