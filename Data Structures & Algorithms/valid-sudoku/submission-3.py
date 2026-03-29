class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(len(board)):
            seenincol = set()
            seeninrow = set()
            for y in range(len(board)):
                if board[x][y] in seeninrow: 
                    return False
                else:
                    if board[x][y]!=".":
                        seeninrow.add(board[x][y])
                
                if board[y][x] in seenincol:
                    return False
                else:
                    if board[y][x]!=".":
                        seenincol.add(board[y][x])
        


        for (a,b) in [(0,3),(3,6),(6,9)]:
            for (c,d) in [(0,3),(3,6),(6,9)]:
                seeninbox = set()
                for i in range(a,b):
                    for j in range(c,d):
                        if board[i][j] in seeninbox:
                            return False
                        else:
                            if board[i][j]!=".":
                                seeninbox.add(board[i][j])
        return True

    


        



                
        