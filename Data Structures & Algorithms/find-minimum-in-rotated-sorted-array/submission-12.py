class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        currmin = 1001

        while l<=r:
            if nums[l] <= nums[r]:
                currmin=min(currmin, nums[l]) # dont forget that this binary search fails for 1 case where the array l to r is already sorted
                # so we need to handle that case seperately here.
            mid = (l+r)//2
            currmin = min(currmin, nums[mid])
            if nums[l]<=nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return currmin