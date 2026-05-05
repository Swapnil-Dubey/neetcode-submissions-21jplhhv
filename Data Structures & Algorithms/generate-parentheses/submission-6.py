class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #input: int n (pairs of parenthesis)
        #output: List of str: all "well formed" parenthesis strings can generate with n pairs of parenthesis
        #constraints: wellformed means: all ( should end with ) and no ) before ( and number of ( == numnber of ) == n
        #edge cases: n== 1 and n == 7
        #pattern and approach: backtracking approach: essentially a DFS with tracking Open and Close counts
        #time complexity: 
        #space complexity: 

        res = []


        def dfs(curr, open, close):
            if open == n and close == n:
                res.append(curr)
                return

            if open<n:
                dfs(curr+"(",open+1,close)
            
            if close<open:
                dfs(curr+")",open,close+1)
            
            




        dfs("",0,0)
        return res
        



