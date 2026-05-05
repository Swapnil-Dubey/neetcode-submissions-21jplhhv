class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # number of coins it takes to get to amount = 
            # min(number of coins it takes to get to amount-coins[i])
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            res = 1e9
            for coin in coins:
                if amount-coin>=0:
                    res = min(res,1+dfs(amount-coin))
            
            memo[amount] = res
            return res
        mincoins = dfs(amount)
        if mincoins>=1e9:
            return -1
        else:
            return mincoins
