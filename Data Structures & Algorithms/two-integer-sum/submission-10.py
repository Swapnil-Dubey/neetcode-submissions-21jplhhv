class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #input = [int] nums, int target
        #output: [int i, int j]; i and j are indices; nums[i]+nums[j]==target
        #constraints: i!=j
        #edge cases: nums[i] == 0, nums[i] == negative
        #brute force: double pass O(n^2)
        # better pattern and approach: hashset: store the elements seen in nums until now (to check for O(1) membership) and seeing if target-curr is present in hashset
        #           otherwise, put curr into hashset

        seen = {}

        for i in range(len(nums)):
            if target-nums[i] in seen:
                return [seen[target-nums[i]],i]
            else:
                seen[nums[i]] = i #{3:0}

        