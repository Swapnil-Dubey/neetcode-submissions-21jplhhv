class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #keep open, close count




        res = []

        def dfs(curr,open,close):
            if open==n and close == n:      # base case
                res.append(curr)
                return
            
            if open<n:                  # we can add open parenthesis only if this is true
                dfs(curr+"(",open+1,close)
            if close<open:              #we can add closing parenthesis only if this is true
                dfs(curr+")",open,close+1)
               

        dfs("",0,0)
        return res
            
