class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #input: int [] nums (rotated sorted arr), int target
        #output: index of target if exists, otherwise -1
        #constraints: 1 <= nums.length <= 1000
#           -1000 <= nums[i] <= 1000
#           -1000 <= target <= 1000

        #edge cases: single length nums
        #pattern: binary search bcz O(logn) search for index
        #approach: set l, r, mid pointers , REMEMBER THAT THIS APPRCH DOESNT WORK FOR EDGES (L and R) so handle them
        #       if value at mid is not target then check for where the pivot is (bcz the other side is gonna be fully sorted)
        #time complexity: O(logn)
        #space complexity: 

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid]==target:
                return mid
            
            # pivot is on right side
            if nums[l]<=nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            #pivot is on left side
            else:
                if nums[mid]<=target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1