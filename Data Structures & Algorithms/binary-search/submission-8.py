class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # distinct ints in nums, sorted in asc

        #return index if exists

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return -1