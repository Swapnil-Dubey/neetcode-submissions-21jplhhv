class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1# min k
        r = max(piles) # max k 
        currkmin = 1000000001
        #k is somewhere in this range
 
        while l<=r:
            mid = (l+r)//2

            #mid = curr k
            # check how many hrs needed to eat all piles within this k

            hrs = 0
            for p in piles:
                hrs+=math.ceil(p/mid)
            if hrs<=h:
                currkmin = min(currkmin, mid)#found this k but still try to go for a smaller k to see if there is one possible?
                r = mid-1
            else:
                l=mid+1
        return currkmin
            
