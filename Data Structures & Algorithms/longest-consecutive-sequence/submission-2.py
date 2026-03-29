class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largestconsec = 1
        snums = set(nums)

        if len(snums) == 0:
            return 0
        else:
            for i in snums:# 2
                curr = 1 
                x = i # 2
                while (x+1) in snums:
                    curr+=1
                    x+=1
                if curr>largestconsec:
                    largestconsec = curr
        return largestconsec