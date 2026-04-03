class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #output = in place modification of surrounded 0s
        # constraints: 1 <= board.length, board[i].length <= 200
#                       board[i][j] is 'X' or 'O'
        # pattern: graphs
        # approach:  reverse way of thinking : everything except non surrounded regions
        #            mark all the Os at borders as T and run DFS on them to mark those as T too
        # time complexity:
        #space complexity: 

        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        borderOs = set()
        unsurrounded = set()

        #find borderOs
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or r == ROWS-1 or c == 0 or c==COLS-1) and board[r][c]=="O":
                    borderOs.add((r,c))

    

        def dfs(r, c):
            nonlocal unsurrounded
            nonlocal visited
            unsurrounded.add((r,c))
            visited.add((r,c))
            if r+1 in range(ROWS) and (r+1,c) not in visited and board[r+1][c]=='O':
                dfs(r+1,c)
            if r-1 in range(ROWS) and (r-1,c) not in visited and board[r-1][c]=='O':
                dfs(r-1,c)
            if c+1 in range(COLS) and (r,c+1) not in visited and board[r][c+1]=='O':
                dfs(r,c+1)
            if c-1 in range(COLS) and (r,c-1) not in visited and board[r][c-1]=='O':
                dfs(r,c-1)

        for (r,c) in borderOs:
            dfs(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) not in borderOs and (r,c) not in unsurrounded:
                    board[r][c] = 'X'


            
