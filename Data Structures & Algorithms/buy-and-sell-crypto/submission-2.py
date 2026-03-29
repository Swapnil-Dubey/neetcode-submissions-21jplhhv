class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force: double for loop O(n^2)

        #2 pointer approach, initialize l = 0, r = l+1, if r+1 is bigger then we sell on that day (r is sell, l is buy)
        #   and note down max profit, but if r+1 is smaller than l then move l to r+1 and r to l+1

        l = 0
        r = l+1
        currprofit = 0
        while r<=len(prices)-1:
            currprofit = max(currprofit,prices[r]-prices[l])
            if prices[r]<prices[l] and r!=len(prices)-1:
                l=r
            r+=1
        return currprofit