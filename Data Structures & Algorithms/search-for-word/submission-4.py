class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visit = set()
        ROW = len(board)
        COL = len(board[0])
    
        def dfs(i, row, col):
            if i == len(word):
                return True
            if row not in range(ROW) or col not in range(COL) or (row,col) in visit or board[row][col]!=word[i]:
                return False
            visit.add((row,col))
            res = dfs(i+1, row+1, col) or dfs(i+1, row-1, col) or dfs(i+1, row, col+1) or dfs(i+1, row, col-1)
            visit.remove((row,col))

            return res


        

        for r in range(ROW):
            for c in range(COL):
                if dfs(0,r,c) == True:
                    return True
        return False