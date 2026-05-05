class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #fewest number of coins needed to make the total = fewest number of coins to make min(1+fn(amount-coins[i]))
        memo = {}
        for coin in coins:
            memo[coin] = 1
        
        def f(n):
            if n == 0:
                return 0 # dont forget base case if n == 0***
            if n in memo:
                return memo[n]
            res = []
            for coin in coins:
                if (n-coin)>=0: # need to make sure the subtraction doesnt lead to a negative result
                    recres = f(n-coin) # save the recursion result to avoid recursing again
                    if recres == -1:
                        continue
                    res.append(recres+1)
            if res == []: # if there is no possible path, this is not calculable so return -1 (imp dont forget to memo this too)
                memo[n] = -1
                return memo[n]
            memo[n] = min(res)
            return memo[n]
        return f(amount)