class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #at each step either include or not inlude the next element in nums

        res = []
        curr = []

        def dfs(i):
            if i == len(nums): # means all elements in nums are done
                res.append(curr.copy())
                return # DONT FORGET TO RETURN
            
            curr.append(nums[i])
            dfs(i+1)

            curr.pop()
            dfs(i+1)

        dfs(0)
        return res
