class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # essentially keep moving the goal post closer until u can reach it from ith position

        goal = len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if nums[i]+i>=goal: #>= bcz jump can be made anywhere from 1 to nums[i]
                goal = i
        if goal == 0:
            return True
        else:
            return False