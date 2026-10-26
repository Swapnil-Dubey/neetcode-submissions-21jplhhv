class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = nums[0]^0

        for i in range(1,len(nums)):
            xor = xor^i^nums[i]
        xor = xor^len(nums)
        
        return xor

        