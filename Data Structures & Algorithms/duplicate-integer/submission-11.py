class Solution:
    def hasDuplicate(self, nums: [int])->bool:
        # edge case: empty array, 1 element
        # normal input: [1,2,2] -> True
                    #   [1,2] -> False
        
        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
        