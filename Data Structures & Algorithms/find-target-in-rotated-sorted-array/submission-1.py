class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #input = [int] nums, int target
        #output  = int indexoftarget or -1
        #constraints = nums oa asc arr posibly rotated
        #brute force = iterate through the array, return index of target when found
        #edge cases = 1 element array, negative target search
        #pattern = binary search


        #approach
        #time complexity
        #space complexity

        for i in range(len(nums)):
            if nums[i]==target:
                return i
        return -1

