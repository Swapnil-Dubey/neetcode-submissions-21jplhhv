class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)

        memo1 = {0:nums[0],1:max(nums[0],nums[1])}
        memo2 = {1:nums[1],2:max(nums[1],nums[2])}
        
        #return max amount of money u can rob at i(inclusive)
        def helper(i, memo):

            if i in memo:
                return memo[i]
            
            memo[i] = max(helper(i-2,memo)+nums[i],helper(i-1,memo))
            return memo[i]
        
        return max(helper(len(nums)-1,memo2),helper(len(nums)-2, memo1))
