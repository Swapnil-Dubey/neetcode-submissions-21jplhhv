class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if currsum< 0 then change left pointer to right pointer
        currsum = 0
        res = -100000000000000
        for i in nums:
            if currsum<0:
                currsum = 0
            currsum+=i
            res = max(res, currsum)
        return res




