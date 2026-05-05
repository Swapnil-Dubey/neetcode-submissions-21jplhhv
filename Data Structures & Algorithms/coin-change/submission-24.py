class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0:0}
        for c in coins:
            memo[c] = 1
        
        #returns min number of coins needed to make up target amount else -1
        def numcoins(amount):
            if amount in memo:
                return memo[amount]
            if amount<0:
                return -1
            res = 100000
            for i in coins:
                recres = numcoins(amount-i)
                if recres!=-1:
                    res = min(res,1+recres)
            
            if res == 100000:
                memo[amount]=-1
                return -1
            else:
                memo[amount] = res
                return res
        return numcoins(amount)
