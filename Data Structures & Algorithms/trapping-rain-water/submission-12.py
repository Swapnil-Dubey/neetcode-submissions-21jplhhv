class Solution:
    def trap(self, height: List[int]) -> int:
        #water[i] = min(maxleft, maxright)-height[i] if sum is +ve

        maxleft = []
        maxright = []

        for i in range(len(height)):
            if i == 0:
                maxleft.append(0)
            else:
                maxleft.append(max(maxleft[i-1],height[i-1]))


        for i in range(len(height)-1,-1,-1):
            if i == len(height)-1:
                maxright.append(0)
            else:
                maxright.append(max(maxright[-1],height[i+1]))
        
        maxright.reverse()

        res = 0

        for i in range(len(height)):
            currsum = min(maxleft[i],maxright[i])-height[i]
            if currsum>0:
                res+=currsum

        return res


