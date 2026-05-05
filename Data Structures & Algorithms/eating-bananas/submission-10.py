class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #input = [int] piles (bananas in ith pile), int h (number of hours you have to eat all bananas)
        #output: int k (bananas per hour eating rate)  : minimum
        #constraints: can't move to a different pile in the same hour (1 pile per hour)**
        #edge cases: 1 pile length, no. of hours = len of piles
        #approach and pattern: binary search on answer space: k has a bounded range of min = 1 and max = max(piles)

        #time complexity: 
        #space complexity:


        l = 1
        r = max(piles)
        res = float('inf')
        while l<=r:
            mid = (l+r)//2
            currhr = 0
            for i in piles:
                currhr+=math.ceil(i/mid)
            if currhr<=h:
                res = min(res, mid)
                r = mid-1
            else:
                l = mid+1
        return res
