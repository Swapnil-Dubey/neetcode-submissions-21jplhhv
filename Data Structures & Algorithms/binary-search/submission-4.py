class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #input = [int] nums, distinct in asc, int target
        #output = int indexoftarget, otherwise -1
        # time complexity = O(logn)

        l = 0
        r = len(nums)-1

        while l<=r: #= also because what if there is only 1 element in the array
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1