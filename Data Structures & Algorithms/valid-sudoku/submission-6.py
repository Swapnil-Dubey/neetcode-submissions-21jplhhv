class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            seeninrow = set()
            seenincol = set()
            for j in range(len(board)):
                if board[i][j]!=".":
                    if board[i][j] in seeninrow:
                        return False
                    else:
                        seeninrow.add(board[i][j])

                if board[j][i]!=".":
                    if board[j][i] in seenincol:
                        return False
                    else:
                        seenincol.add(board[j][i])
        
                
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
                