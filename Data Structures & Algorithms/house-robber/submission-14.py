class Solution:
    def rob(self, nums: List[int]) -> int:
        #nums [i] = amount of money at house ith

        #cant rob two adjacent houses
        #   this means we can either rob n-2th + nth house or n-1th house

        #trick is that: max amount of money we can rob until and inclusive of n = max(money at nth + recursive(n-2),(recursive call to n-1))


        if len(nums)==1:
            return nums[0]

        d = {0:nums[0],1:max(nums[0],nums[1])} ## fill this

        def dfs(i):

            if i in d:
                return d[i]
            
            d[i] = max(dfs(i-2)+nums[i],dfs(i-1))
            return d[i]
        
        return dfs(len(nums)-1)

        

            