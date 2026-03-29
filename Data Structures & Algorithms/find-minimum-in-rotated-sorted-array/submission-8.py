class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        currmin = math.inf

        
        while l<=r:
            mid = (l+r)//2
            currmin = min(currmin, nums[mid], nums[l])

            if nums[l]<=nums[mid]:#it means list towards the left of mid is all sorted in in increasing order
                l =mid+1
            else:
                r=mid-1
        return currmin        
        