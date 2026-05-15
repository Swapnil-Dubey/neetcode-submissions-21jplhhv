class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #int [] nums, int target
        #output: [[]] int: all combinations of nums that sum to target

        #constraints: same number can be chosen unlimited times

        #approach and pattern: backtracking: either stay on current number and add to currsum or move onto next number

        res = []

        def dfs(i,curr,currsum):
            if currsum>target or i>len(nums)-1:
                return
            if currsum==target:
                res.append(curr.copy())
                return

            

            curr.append(nums[i])
            dfs(i,curr,currsum+nums[i])

            curr.pop()
            dfs(i+1,curr,currsum)
        

        dfs(0,[],0)


        return res
