class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = l+1
        if len(prices)==1:
            return 0
        currprofit = 0
        while r<len(prices):
            currprofit = max(currprofit,prices[r]-prices[l])
            if prices[r]<prices[l]:
                l = r
            r+=1
        return currprofit
                

