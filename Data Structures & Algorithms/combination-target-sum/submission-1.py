class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i):
            if i>=len(nums):
                return
            if sum(curr)>target:
                return
            if sum(curr) == target:
                res.append(curr.copy())
                return #dont forget to return after the base case ****
            
            

            curr.append(nums[i])
            dfs(i)

            curr.pop()
            dfs(i+1)
        dfs(0)
        return res