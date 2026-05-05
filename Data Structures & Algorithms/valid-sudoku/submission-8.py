class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check row and col
        currrow = set()


        for r in range(len(board)):
            currrow = set()
            currcol = set()
            for c in range(len(board)):
                if board[r][c]!=".":
                    if board[r][c] in currrow:
                        return False
                    else:
                        currrow.add(board[r][c])
                if board[c][r]!=".":
                    if board[c][r] in currcol:
                        return False
                    else:
                        currcol.add(board[c][r])
        for (m,n) in [(0,3),(3,6),(6,9)]:
            for (p,q) in [(0,3),(3,6),(6,9)]:
                seeninbox = set()
                for i in range(m,n):
                    for j in range(p,q):
                        if board[i][j]!= ".":
                            if board[i][j] in seeninbox:
                                return False
                            else:
                                seeninbox.add(board[i][j])
          
        return True


        

        

            