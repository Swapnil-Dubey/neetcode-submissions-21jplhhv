class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #min number of coins to make up n amount = 
        #   min coins to make up amount-i amount + 1


        memo = {}
        for i in coins:
            memo[i] = 1
        

        def dfs(amt):
            if amt == 0:
                return 0
            if amt<0:
                return -1

            if amt in memo:
                return memo[amt]
            
            curr_res = float("inf")
            for i in coins:
                recres = dfs(amt-i)
                if recres == -1:
                    memo[amt] = -1
                    continue
                curr_res= min(curr_res,recres+1)
            if curr_res == float("inf"):
                return -1
            
            memo[amt] = curr_res
            return memo[amt]
        
        return dfs(amount)
        