class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums)==2:
            return max(nums)

        memo1 = {0:nums[0],1:max(nums[0],nums[1])}
        memo2 = {1:nums[1],2:max(nums[1],nums[2])}
        
        def maxcash(i, memo):
            if i in memo:
                return memo[i]
            memo[i] = max(maxcash(i-1, memo),maxcash(i-2, memo)+nums[i])
            return memo[i]

        return max(maxcash(len(nums)-1,memo2), maxcash(len(nums)-2,memo1))