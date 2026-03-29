class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # data structure: hashset (search in O(1))
        # time complexity target: O(n)
        # edge cases: nums is empty, single element

        prev = set()
        for num in nums:
            if num in prev:
                return True
            else:
                prev.add(num)
        return False