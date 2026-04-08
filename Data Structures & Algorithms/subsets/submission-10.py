class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # at each step choose to either include or not include the current number

        res = []
        curr = []

        def dfs(i):
            if i>=len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i+1)

            curr.pop()
            dfs(i+1)
        dfs(0)
        return res