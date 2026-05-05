class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        

        for r in range(ROWS):
            seeninrow = set()
            seenincol = set()
            for c in range(COLS):
                

                if board[r][c] in seeninrow:
                    return False
                else:
                    if board[r][c]!='.':
                        seeninrow.add(board[r][c])
                

                if board[c][r] in seenincol:
                    return False
                else:
                    if board[c][r]!='.':
                        seenincol.add(board[c][r])
        
        for (m,n) in [(0,3),(3,6),(6,9)]:
            for (p,q) in [(0,3),(3,6),(6,9)]:
                seeninbox = set()
                for r in range(m,n):
                    for c in range(p,q):
                        if board[r][c] in seeninbox:
                            return False
                        else:
                            if board[r][c]!='.':
                                seeninbox.add(board[r][c])
        return True

                