class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = ""

        def dfs(close, open):
            nonlocal curr # remember to do non local curr bcz strings are immutable so curr+=")" is essentialle declaring a new local var within the function
            if len(curr) == n*2:
                res.append(curr)
                return
            
            if open<n:
                curr+="("
                dfs(close,open+1)
                curr=curr[:-1]
            if close<open:
                curr+=")"
                dfs(close+1,open)
                curr = curr[:-1]
        dfs(0,0)
        return res
            
        