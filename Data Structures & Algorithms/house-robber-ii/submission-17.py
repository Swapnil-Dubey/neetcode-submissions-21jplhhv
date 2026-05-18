class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums)==2:
            return max(nums[0],nums[1])
        if len(nums)==1:
            return nums[0]
        
        memo1 = {0:nums[0],1:max(nums[0],nums[1])}
        memo2 = {1:nums[1],2:max(nums[1],nums[2])}

        def dfs(i, memo):
            if i in memo:
                return memo[i]
            
            memo[i] = max(dfs(i-2, memo)+nums[i],dfs(i-1, memo))

            return memo[i]

        return max(dfs(len(nums)-2,memo1),dfs(len(nums)-1,memo2))
        