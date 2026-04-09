class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #input = 2d grid
        #output = true if word in grid
        #pattern: backtracking
        #approach: go down a path only if the letter u are searching for is at that position
        #constraints:
        #edge cases = 
        #time complexity =
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(i, x, y):
            #if we're done with the word
            if i==len(word):
                return True
            # if the position is not the char im looking for: dont explore this path further
            if x not in range(ROWS) or y not in range(COLS) or board[x][y] != word[i] or (x,y) in visited :
                return False
            
            
            # if the position im at is the char im looking for
            visited.add((x,y))
            res = False
            res = res or dfs(i+1, x+1, y)
            res = res or dfs(i+1, x-1, y)
            res = res or dfs(i+1, x, y-1)
            res = res or dfs(i+1, x, y+1)
            visited.remove((x,y))

            return res

        for x in range(ROWS):
            for y in range(COLS):
                if dfs(0,x,y) == True:
                    return True
        return False


            



