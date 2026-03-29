class Solution:
    def search(self, nums: List[int], target: int) -> int:

        #input = int [] nums sorted asc, int target
        #output = int indexoftarget otherwise -1
        #constraints= all integers in nums are unique, nums[i] can be negative too 
        #edge cases = nums is empty, nums is 1 element which is the target
        #pattern = binary earch O(log n)
        #time complexity
        #space complexity

        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2

            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1
