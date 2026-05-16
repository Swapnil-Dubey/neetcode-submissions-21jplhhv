class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #first we'll start dfs at border Os and mark all Os that are rechable from those . otherwise change everything to X
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        unsurrounded = set()





        def dfs(r,c):
            visited.add((r,c))
            unsurrounded.add((r,c))


            if (r+1)>=0 and (r+1)<=ROWS-1 and board[r+1][c]=='O' and (r+1,c) not in visited:
                dfs(r+1,c)
            if (r-1)>=0 and (r-1)<=ROWS-1 and board[r-1][c]=='O' and (r-1,c) not in visited:
                dfs(r-1,c)
            if (c+1)>=0 and (c+1)<=COLS-1 and board[r][c+1]=='O' and (r,c+1) not in visited:
                dfs(r,c+1)
            if (c-1)>=0 and (c-1)<=COLS-1 and board[r][c-1]=='O' and (r,c-1) not in visited:
                dfs(r,c-1)




        

        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c==COLS-1) and board[r][c]=="O":
                    dfs(r,c)
    


        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in unsurrounded:
                    board[r][c]="X"


        