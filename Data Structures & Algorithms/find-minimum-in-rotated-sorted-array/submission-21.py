class Solution:
    def findMin(self, nums: List[int]) -> int:
        #min is gonna be where the pivot is


        l = 0
        r = len(nums)-1
        res = float('inf')

        while l<=r:
            mid = (l+r)//2
            res = min(res,nums[mid], nums[l], nums[r])

            if nums[l]<=nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return res