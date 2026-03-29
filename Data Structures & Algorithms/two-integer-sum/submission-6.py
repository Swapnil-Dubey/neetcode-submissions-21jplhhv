class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # requires: array nums, integer target
        # returns: 1 pair of indexes, smallest first
        # assumptions: only 1 valid answer exists

        #edge cases: example 3
        #data structure: dict (O(1) key lookup time and can map key (num)
            #                                            to values (index)
        # target time complexity = O(n): single pass
        hist = dict()
        for num in range(len(nums)):
            if (target-nums[num]) in hist:
                return [hist[target-nums[num]],num]
            else:
                hist[nums[num]] = num
        return False


