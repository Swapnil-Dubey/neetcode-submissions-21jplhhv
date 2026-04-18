class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)

        memo1 = {0:nums[0],1:max(nums[0],nums[1])}
        memo2 = {0:nums[1],1:max(nums[1],nums[2])}
        
        #return max amount of money u can rob at i(inclusive)
        def helper(i, arr, memo):

            if i in memo:
                return memo[i]
            
            memo[i] = max(helper(i-2, arr, memo)+arr[i],helper(i-1, arr,memo))
            return memo[i]
        
        return max(helper(len(nums)-2, nums[1:], memo2),helper(len(nums)-2, nums[0:-1], memo1))
