class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longestlen = 0
        for i in nums:
            if i-1 not in nums: # marks the start of a new sequence
                currlen = 1
                curr = i
                while (curr+1) in nums:
                    curr+=1
                    currlen+=1
                longestlen = max(longestlen,currlen)
            else:
                continue
        return longestlen

