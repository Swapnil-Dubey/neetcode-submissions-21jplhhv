class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #int array prices
        # buy first then sell on a separate day

        #optimize for max profit

        #if profit<0: return 0
        # return max profit


        # input = int [] prices
        # edge case:prices len == 1 (buy and sell date cant be same so return 0 profit)
        # approach: two pointer, b = buy date, s = sell date (always b<s), move check s-b log it, move b to s only if s<b and s +=1 otherwise b stays where it is, s moves ahead. as soon as s hits end of array return currently maintained max profit
        # example walk through:  done
        # time complexity:  O(n)


        b = 0
        s = 1

        if len(prices)==1:
            return 0

        res = 0 #curr max profit
        

        while s<len(prices) and b<s:
            if prices[s]-prices[b]>0:
                res = max(res,prices[s]-prices[b])
                s+=1
            else:
                b = s
                s+=1
        return res


