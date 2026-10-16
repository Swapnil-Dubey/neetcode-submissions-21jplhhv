class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #edge case
        #normal case
        #better = serach for pivot, then if u found it both either sides are sorted



        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            elif nums[l]<=nums[mid]:
                # left sorted portion
                if nums[l]<=target<=nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            else:
                #right sorted portion
                if nums[mid]<=target<=nums[r]:
                    l = mid+1
                else:
                    r=mid-1
        return -1
