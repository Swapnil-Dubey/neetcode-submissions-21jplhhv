class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxvol = 0
        l = 0
        r = len(heights)-1

        while l<r:
            currvol = min(heights[l],heights[r])*(r-l)
            maxvol = max(maxvol, currvol)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return maxvol