class Solution:
    def search(self, nums: List[int], target: int) -> int:

#constraints:
#edge cases: 1 element array
#pattern: binarysearch
#approach: rotated array, search for index of target -> start by setting up search pivot
# 
#time complexity: O(logn)

        l =0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            elif target == nums[mid]:
                return mid
            #rememner that in a rotated sorted array 1 side of mid and/or pivot is sorted (either left or right)

            # left part is sorted:
            if nums[l]<=nums[mid]:
                if nums[l]<=target<=nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            #right part is sorted
            else:
                if nums[mid]<=target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
        return -1
