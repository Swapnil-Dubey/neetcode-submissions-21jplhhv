class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #input = int [] prices
        #output = int maximum_profit

        #constraints: buy day != sell day, sell day > buy day
        #             min profit = 0 

        #edge cases: 0 or negative profit in prices, len(prices) == 1


        # brute force: 2 for loop (nested loop): O(n^2)
        #pattern and better approach: two pointer approach to the problem, O(n): one pass

        l = 0 # buy
        r = 1 # sell 
        #l<r
        res = 0

        if len(prices) == 1:
            return 0
        
        while r<=len(prices)-1:
            res = max(res, prices[r]-prices[l])

            if prices[r]<prices[l]:
                l = r
            
            r+=1
        return res