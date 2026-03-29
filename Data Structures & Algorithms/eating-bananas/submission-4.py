class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #constraints: if pile has less than k bananas, cant eat from another pile,  so k has to be max number in the piles arr
        #   bcz we dont need higher than that as h is at least len(piles) and we cant eat from another pile until the end of the hour

        # binary search on k (where k is bounded by min = 1, max = max number of piles array -> at each k we calc hours needed so
        #O(nlogm) where n is the size of piles and m is the max number in piles


        # we want to minimize k

        l = 1 # imp k cant be 0 so l = 1
        r = max(piles)
        currmink = math.inf
        while l<=r:
            k = (l+r)//2
            hoursneeded= 0
            for i in piles:
                hoursneeded+=math.ceil(i/k)
            if hoursneeded>h:
                l=k+1
            else:
                currmink = min(currmink, k)
                r=k-1
        return currmink
                

