class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else: 
                prefix[i] = prefix[i-1] * nums[i]


        numrev = nums.copy()
        numrev.reverse()

        for i in range(len(numrev)):
            if i == 0:
                suffix[i] = numrev[i]
            else: 
                suffix[i] = suffix[i-1] * numrev[i]
        suffix.reverse()


        out = [1]*len(nums)

        for i in range(len(out)):
            if i == 0:
                out[i] = suffix[i+1]
            elif i == len(out)-1:
                out[i] = prefix[i-1]
            else:
                out[i] = prefix[i-1] * suffix[i+1]




        return out
        