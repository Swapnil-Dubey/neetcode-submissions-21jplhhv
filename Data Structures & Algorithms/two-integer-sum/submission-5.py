class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #i!=j, assume 1 solution
        #return smallest index (start iteration from left)
        for i in range(len(nums)): #0,1
            find = target-nums[i]#5
            if find in nums[i+1:]:
                return[i,nums.index(find,i+1)]
        return None