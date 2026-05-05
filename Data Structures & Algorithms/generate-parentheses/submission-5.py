class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #input = int n
        #output = List[str] res (all well formed parenthesis that can be generated with n pairs of parenthesis)
        #constraints: well formed = every ( is closed with ) and no ) comes before its corresponding (
        #edge cases: n = 1, n = 7
        #time complexity: 
        #space complexity:
        #approach and pattern: backtracking, with open and closed in tracking

        res = []


        def dfs(curr, open, close):
            if len(curr)==n*2:
                res.append(curr) # base case (when is curr complete)
            if open<n:
                dfs(curr+'(',open+1,close)
            if close<open:
                dfs(curr+')',open,close+1)
            
            

    


        dfs("",0,0)
        return res