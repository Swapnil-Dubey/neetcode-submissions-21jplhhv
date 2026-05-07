class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 1 # imppp dont forget edge case of single element array or an array with maxseq len == 1
        if len(nums)==0:
            return 0
        for i in nums:
            if i-1 not in nums and i+1 in nums:#starting of a sequence
                j = i
                currlen = 1 
                while j+1 in nums:
                    currlen+=1
                    j+=1
                res = max(res,currlen)
        return res




            

