class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #nums = unique integers
        #returns: all subsets of nums
        #       no duplicate subsets


        # for every number we have 2 options - include or exclude it
        res = []


        def dfs(i,curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i+1,curr)

            curr.pop()

            dfs(i+1, curr)
        

        dfs(0,[])

        return res