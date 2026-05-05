class Solution:
    def trap(self, height: List[int]) -> int:
        #input = [int] height (height of bar)
        #output = max water between bars
        #constraints: 1<=len(height)<=1000
        #             0<=height[i]<=1000
        #edge cases: len(height) == 1
                #    all height[i] == 0
                #    all heights are equal
                #    bell curve (no water can be stored)
        # pattern and approach: two arrays, water storable at i = min(max height towards left of ith, max height towards right of ith)-height at ith
        #time complexity: O(n)
        #space complexity:O(n)

        left = [] # max towards the left of i (exclusive)
        right = [] # max towards the right of i (exclusive)

        currmax = 0
        for i in range(len(height)):
            if i == 0:
                left.append(currmax)
            else: 
                currmax = max(currmax, height[i-1])
                left.append(currmax)
        currmax = 0
        for i in range(len(height)-1, -1, -1):
            if i == len(height)-1:
                right.append(currmax)
            else: 
                currmax = max(currmax, height[i+1])
                right.append(currmax)

        

        res = 0

        for i in range(len(height)):
            if min(left[i],right[-i])-height[i]>0:
                res+=min(left[i],right[-i])-height[i]
        return res


            

