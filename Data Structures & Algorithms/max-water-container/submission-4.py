class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #input = int []
        #output = int

        #area = width * min(height1,height2)

        l = 0
        r = len(heights)-1
        currmax = 0
        while l<r:
            currmax = max((r-l)*min(heights[l],heights[r]),currmax)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return currmax
