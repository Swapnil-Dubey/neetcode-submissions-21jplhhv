class Solution:
    def findMin(self, nums: List[int]) -> int:
#edge cases: 1 element array, 
#pattern: Binary search
#approach: Binary search for the pivot
#time complexity: O(logn)

        l = 0
        r = len(nums)-1
        currmin =1001
        while l<=r:
            mid= (l+r)//2
            currmin = min(nums[mid],currmin, nums[l], nums[r])
            
            if nums[l]<=nums[mid]:
                l = mid+1
            else:
                r=mid-1
        return currmin