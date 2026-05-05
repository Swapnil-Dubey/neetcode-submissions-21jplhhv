class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #decision tree where at each step we either choose the current number
        #   or we choose the next number
        res = []

        def dfs(i, curr, currsum):
            if currsum == target:
                res.append(curr.copy()) # imp remember if we append curr its just gonna append 
                #                           a reference to curr not a snapshot
                return
            if currsum>target or i>len(nums)-1:
                return

            curr.append(nums[i])
            dfs(i, curr,currsum+nums[i])

            curr.pop()
            dfs(i+1, curr,currsum)

        dfs(0,[],0)
        return res
