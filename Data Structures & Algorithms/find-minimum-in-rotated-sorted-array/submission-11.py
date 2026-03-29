class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        currmin = 1001

        while l<=r:
            if nums[l] <= nums[r]:
                currmin=min(currmin, nums[l])
            mid = (l+r)//2
            currmin = min(currmin, nums[mid])
            if nums[l]<=nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return currmin