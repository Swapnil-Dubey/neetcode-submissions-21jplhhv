class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # search according to pivot, as everything on the other side of pivot is sorted

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
                

            #pivot on left
            if nums[l]>nums[mid]:
                if nums[mid]<=target<=nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                if nums[l]<=target<=nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return -1
            
            