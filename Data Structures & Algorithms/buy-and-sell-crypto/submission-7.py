class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #input: list of int: prices
        #output: max possible profit ( choose single day to buy and different future day to sell)
            #   if not possible profit then return 0
#constraints: 1 <= prices.length <= 100
#               0 <= prices[i] <= 100
#edge cases: len(prices) array = 1, prices [0] is 0 with only 1 element
#pattern: Sliding window because 2 pointer approach, buy is always behind sell (contiguos sub array)
#approach: start at first 2 indexes, keep track of max profit, if nums[r+1] is higher than nums[r] then
    # then move the buy pointer(r) to that one and keep l at l, otherwise if r+1 is less than r and less than l so move r to r+2 and move l to r+1 and so on
#time complexity: O(n)
#space complexity: O(1)
        l = 0
        r = l+1
        if len(prices)==1:
            return 0

        currmaxprofit = 0
        while r<len(prices):
            currmaxprofit = max(currmaxprofit, prices[r]-prices[l])

            if prices[r]<prices[l]:
                l = r
                r = l+1
            else:
                r+=1

                
        return currmaxprofit