class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = candidates
        nums.sort()
        curr = []
        res = []

        def dfs(i, currsum):
            if currsum==target:
                res.append(curr.copy())
                return
            if currsum>target or i>=len(nums):
                return
            
            curr.append(nums[i])
            dfs(i+1,currsum+nums[i])

            curr.pop()
            while i+1<len(nums) and nums[i+1]==nums[i]:
                i+=1
            dfs(i+1,currsum)
        dfs(0,0)
        return res