class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #cycle detection problem because O(1) extra space
        #2 key things that allow us to solve this question is: 
        #   nums[i] isin [1,n]
        #   len(nums) = n+1

        slow = 0 #start these pointers at index i = 0
        fast = 0

        while True: 
            slow = nums[slow] # = 1
            fast = nums[nums[fast]] # = 2
            if slow == fast:
                break

        slow1 = 0
        slow2 = slow

        while True:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
            if slow1 == slow2:
                return slow1
            