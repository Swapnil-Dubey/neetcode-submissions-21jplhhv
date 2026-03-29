class Solution:
    def findMin(self, nums: List[int]) -> int:
        #search for the pivot

        l =0
        r = len(nums)-1
        currmin = 1001

        while l<=r:
            mid = (l+r)//2
            currmin = min(currmin, nums[mid], nums[l], nums[r])

            if nums[l]<=nums[mid]:
                #pivot is on right side
                l = mid+1
            else:
                r = mid-1
        return currmin