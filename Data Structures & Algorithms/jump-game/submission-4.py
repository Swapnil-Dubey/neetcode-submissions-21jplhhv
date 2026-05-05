class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #keep moving our flag from end of the list towards the front if we can reach index 0, then true

        goal = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i+nums[i]>=goal:
                goal= i
            
        return goal == 0

        