class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        curr = []
        res = []

        def dfs(i, currsum):
            if currsum==target:
                res.append(curr.copy())
                return
            if currsum>target or i>=len(nums):
                return
            
            curr.append(nums[i])
            dfs(i,currsum+nums[i])

            curr.pop()
            dfs(i+1,currsum)
        dfs(0,0)
        return res