class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        currmaxprofit = 0

        if len(prices) == 1:
            return 0

        while r<len(prices):
            currmaxprofit = max(currmaxprofit, prices[r]-prices[l])
            if prices[l]>prices[r]:
                l = r
            r+=1
        return currmaxprofit

