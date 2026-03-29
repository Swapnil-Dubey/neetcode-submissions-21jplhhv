class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        curr = {}
        currlargest = 0
        nums = list(set(nums))
        for i in nums:
            if i-1 not in nums:
                num = i
                numlist = [num]
                while num+1 in nums:
                    numlist.append(num+1)
                    num+=1
                if len(numlist)>currlargest:
                    currlargest = len(numlist)
                curr[i] = numlist
        return currlargest
        
                
