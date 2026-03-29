class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1 # imp keep sure to remember k(eating rate) cant be 0 here
        r = max(piles)
        currk = 1000000001
        while l<=r:
            mid = (l+r)//2
            currh = 0
            for p in piles:
                currh+=math.ceil(p/mid)
            
            if currh<=h:
                currk = min(currk,mid)
                r=mid-1
            else:
                l=mid+1
        return currk


