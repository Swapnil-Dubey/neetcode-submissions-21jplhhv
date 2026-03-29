class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input = [int]
        #output = int

        maxlongest = 0

        nums = set(nums)


        for n in nums:
            if (n-1) not in nums:
                #this is the start of a potential seq
                curr = n
                currlength = 1
                while curr+1 in nums:
                    curr+=1
                    currlength+=1
                maxlongest = max(maxlongest, currlength)
        return maxlongest


        