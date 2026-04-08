class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = ""

        def dfs(open, close):
            nonlocal curr
            if len(curr)==n*2:
                res.append(curr)
                return
            
            if open<n:
                curr+='('
                dfs(open+1, close)
                curr = curr[:-1]
            if close<open:
                curr+=')'
                dfs(open, close+1)
                curr = curr[:-1]
        dfs(0,0)
        return res

        