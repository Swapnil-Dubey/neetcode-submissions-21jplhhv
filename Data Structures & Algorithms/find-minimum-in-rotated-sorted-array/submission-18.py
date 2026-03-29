class Solution:
    def findMin(self, nums: List[int]) -> int:
#input: int[n] rotated sorted array
#output: int res (minimum element in nums)
#constraints:1 <= nums.length <= 1000
#           -1000 <= nums[i] <= 1000

#edge cases:nums is length 1, 2 elements but both are equal
#pattern: serach for the pivot (that's gonna have the minimum element)
#approach: binary search for the pivot (as the side that doesnt have the pivor is gonna be sorted so dont search there)

#time complexity:O(logn)
#space complexity:O(1)
        l = 0
        r = len(nums)-1
        res = 1001

        while l<=r:
            mid = (l+r)//2

            #check curr mid value for min
            res = min(res, nums[mid], nums[l]) # when seraching for pivot, u 
            #           see here that go fot the side that has the pivot but what if there is not pivot
            #           and the entire subrange is sorted. then the leftmost element of the sorted side is gonna
            #           be the minimum one. So check that too! nums[l]

            #right side has the pivot
            if nums[l]<=nums[mid]:
                l = mid+1 #search the right side
            else:
                r = mid-1
        return res