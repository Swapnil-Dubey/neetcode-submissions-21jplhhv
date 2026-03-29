class Solution:
    def search(self, nums: List[int], target: int) -> int:

#constraints: nums elements are unique, rotated ascending array
#edge cases: nums length == 1, 2
#pattern:binary search
#approach: return index of target otherwise -1, -> search for pivot(other half is gonna be sorted sub array)
#time complexity:O(logn)

        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2

            if target ==nums[mid]:
                return mid
            elif target == nums[l]:
                return l
            elif target == nums[r]:
                return r

            # left side is sorted (right has the pivot)
            if nums[l]<=nums[mid]:
                if nums[l]<target<nums[mid]:
                    r=mid-1
                else:
                    l = mid+1
            #right side is sorted (left has the pivot)
            else:
                if nums[mid]<target<nums[r]:
                    l = mid+1
                else:
                    r = mid-1
                
        return -1

