class Solution:
    def trap(self, height: List[int]) -> int:
        # input = [int] height, each bar has width 1
        #output = int maxarea (that can be trapped between bars)

        #trappable water at position i = min(maxleftwall[i], maxrightwall[i])-height[i]
        maxleftwall = [0]*len(height)
        maxrightwall = [0]*len(height)
        result = 0

        currmax = 0
        for i in range(len(height)):
            maxleftwall[i] = currmax
            currmax = max(currmax, height[i])
        
        currmax = 0
        for i in range(len(height)-1,-1,-1):
            maxrightwall[i] = currmax
            currmax = max(currmax, height[i])
        

        for i in range(len(height)):
            if height[i]<min(maxleftwall[i],maxrightwall[i]):
                result += min(maxleftwall[i],maxrightwall[i])-height[i]

        return result
        

