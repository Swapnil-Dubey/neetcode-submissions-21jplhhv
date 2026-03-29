class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = []

        def dfs(close, open):
            if len(curr)==n*2:
                res.append("".join(curr))
                return


            
            if open<n:
                curr.append("(")
                dfs(close,open+1)
                curr.pop()

            

            if close<open:
                curr.append(")")
                dfs(close+1,open)
                curr.pop()
            
        dfs(0,0)
        return res