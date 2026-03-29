class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets = set()
        for i in nums:
            if i in sets:
                return True
            else:
                sets.add(i)
        return False