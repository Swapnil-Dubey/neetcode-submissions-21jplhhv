class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #either take the current number, if taken then u dont need while loop
        # if u skip it though, u need to skil all instances of it (right side of the tree)

        

        res = []
        curr = []
        nums.sort()
        def dfs(i):
            if i>=len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i+1)

            curr.pop()
            while i+1<len(nums) and nums[i+1]==nums[i]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res