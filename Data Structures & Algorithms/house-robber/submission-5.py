class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)

        memo = {0:nums[0],1:max(nums[0],nums[1])}
        
        #return max amount of money u can rob at i(inclusive)
        def helper(i):

            if i in memo:
                return memo[i]
            
            memo[i] = max(helper(i-2)+nums[i],helper(i-1))
            return memo[i]
        
        return helper(len(nums)-1)
