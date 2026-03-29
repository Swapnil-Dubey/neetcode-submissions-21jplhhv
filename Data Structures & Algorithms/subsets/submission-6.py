class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #at each step either include or not inlude the next element in nums

        res = [] # final list of all subsets
        curr = [] # current subset being built

        def dfs(i):
            if i == len(nums): # means all elements in nums are done ( reach end of array, this represents 1 subset so store it)
                res.append(curr.copy())
                return # DONT FORGET TO RETURN
            
            curr.append(nums[i]) # add the current number
            dfs(i+1) #explore further

            curr.pop() # remove the number (undo) - BACKTRACK
            dfs(i+1) # explore without it


        dfs(0)
        return res # this generates all 2**n subsets
