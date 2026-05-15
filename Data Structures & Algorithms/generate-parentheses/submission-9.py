class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #keep open, close count




        res = []

        def dfs(curr,open,close):
            if open==n and close == n:
                res.append(curr)
                return
            
            if open<n:
                dfs(curr+"(",open+1,close)
            if close<open:
                dfs(curr+")",open,close+1)
               

        dfs("",0,0)
        return res
            
