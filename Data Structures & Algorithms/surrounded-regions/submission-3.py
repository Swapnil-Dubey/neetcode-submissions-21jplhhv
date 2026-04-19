class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #not surrounded are the ones reachable by Os on the edges

        ROWS = len(board)
        COLS = len(board[0])
        unsurrounded = set()
        visited = set()


        def dfs(r,c):
            unsurrounded.add((r,c))


            if r+1 in range(ROWS) and (r+1,c) not in visited and (r+1,c) not in unsurrounded and board[r+1][c]=='O':
                dfs(r+1,c)
            if r-1 in range(ROWS) and (r-1,c) not in visited and (r-1,c) not in unsurrounded and board[r-1][c]=='O':
                dfs(r-1,c)
            if c+1 in range(COLS) and (r,c+1) not in visited and (r,c+1) not in unsurrounded and board[r][c+1]=='O':
                dfs(r,c+1)
            if c-1 in range(COLS) and (r,c-1) not in visited and (r,c-1) not in unsurrounded and board[r][c-1]=='O':
                dfs(r,c-1)




        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c == COLS-1) and board[r][c]=='O':
                    dfs(r,c)
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c]=='O' and (r,c) not in unsurrounded:
                    board[r][c]='X'
        
        


