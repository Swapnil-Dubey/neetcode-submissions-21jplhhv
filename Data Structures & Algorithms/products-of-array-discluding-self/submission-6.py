class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                prefix[i] = prefix[i-1]*nums[i-1]
        
        suffix = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            if i == len(nums)-1:
                continue
            else:
                suffix[i] = suffix[i+1]*nums[i+1]
        

        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i]*suffix[i]
        
        return res

