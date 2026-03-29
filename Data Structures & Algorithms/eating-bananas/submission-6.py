class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # realize that k is bounded, binary search on k


        l = 1
        r = max(piles)
        currmin = max(piles)

        while l<=r:
            mid = (l+r)//2

            timereqd = 0
            for i in piles:
                timereqd+=math.ceil(i/mid)
            
            if timereqd<=h:
                currmin = min(currmin, mid)
                r = mid-1
            else:
                l = mid+1
        return currmin
