class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setnums = set(nums)
        res = 1
        curr_res = 1
        if not nums:
            return 0
        for i in nums:
            if i-1 in setnums:#not a start of seq
                continue
            else: # is a start of seq
                curr = i
                while curr+1 in setnums:
                    curr+=1
                    curr_res+=1
                res = max(res, curr_res)
                curr_res = 1
            
        return res
                

                

        