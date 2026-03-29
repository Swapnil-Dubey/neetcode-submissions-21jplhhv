class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
#input: int[] piles, int h
#output: int k (bananas per hour)
#constraints: each hour you can eat k bananas from max 1 pile (cant switch to another pile in the same hour)
#   1 <= piles.length <= 1,000
#   piles.length <= h <= 1,000,000
#   1 <= piles[i] <= 1,000,000,000
#edge cases: len(piles) ==1
#pattern: Binary search
#approach: k is bounded [1,max(piles)] binary search on that
#time complexity: O(n*logm)
#space complexity: 

        l = 1
        r = max(piles)
        currmin = r
        while l<=r:
            mid = (l+r)//2
            
            hours = 0
            for i in piles:
                hours+=math.ceil(i/mid)
            
            if hours>h:
                l = mid+1
            else:
                currmin = min(currmin, mid)
                r = mid-1
        return currmin



