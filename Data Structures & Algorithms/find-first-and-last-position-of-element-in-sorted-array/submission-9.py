class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1

        currbestl = 1e9
        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                currbestl = min(currbestl,mid)
                r = mid-1
                

            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        if currbestl == 1e9:
            return [-1,-1]


        l = 0
        r = len(nums)-1
        currbestr = 0
        while l<=r:
            mid = (l+r)//2

            if nums[mid] == target:
                currbestr = max(currbestr,mid)
                l = mid+1
                

            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return [currbestl, currbestr]

            