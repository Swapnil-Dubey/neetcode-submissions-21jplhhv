class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#input: int [] prices
#output: int maxprofit
#constraints:1 <= prices.length <= 100
#            0 <= prices[i] <= 100
#edge cases:decreasing values, single element in prices
#pattern: Sliding window
#approach:start l at index 0, r at index 1 then check r+1, if its lower than l then move l there and move r to r+1, otherwise move r there
#time complexity:O(n)
#space complexity:

        if len(prices)==1:
            return 0

        l = 0
        r = l+1
        currmax = 0

        while r<len(prices):
            currmax = max(currmax,prices[r]-prices[l])
            if r<len(prices)-1 and prices[r]<prices[l]:
                l = r
                r= l+1
            else:
                r+=1
        return currmax
