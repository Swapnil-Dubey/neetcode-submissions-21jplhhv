class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currsum = 0

                #just go through the array, removing any negative prefix
        for i in range(len(nums)):
            if currsum<0:
                currsum = 0
            currsum+=nums[i]

            res = max(currsum,res)
        return res