class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # input = [int] nums : sorted ASC, int target
        # output = starting and ending position of target value in nums
        #       if not found return [-1,-1]
        # constraints: ologn time complexity: Binary Search
        #           0<=len(nums)
        #           nums is sorted ASC

        # edge cases: len(nums) == 0 or 1
        #            target is not in nums
        #            target is the only thing in the array

        # approach and pattern: binary search on array index, given nums is sorted

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                r = mid-1


            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        resl = l
        
        if resl>len(nums)-1 or nums[resl]!=target:
            resl = -1

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                l = mid+1


            elif nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
        resr = r
        if resr<0 or nums[resr]!=target:
            resr = -1
            
        return [resl,resr]
            
