class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # as long as in the range(mxn) , at each position we can either choose to go down or right


        memo = {}

        def dfs(x,y):
            if (x,y) == (m-1,n-1):
                memo[(x,y)] = 1
                return memo[(x,y)]
            if x<0 or x>=m or y<0 or y>=n:
                return 0
            if (x,y) in memo:
                return memo[(x,y)]
            
            memo[(x,y)] = dfs(x+1,y) + dfs(x,y+1)
            return memo[(x,y)]



        return dfs(0,0)