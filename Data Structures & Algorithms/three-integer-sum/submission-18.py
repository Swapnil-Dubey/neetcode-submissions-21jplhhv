class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: # why do we need this
                continue
            l = i+1 # 1
            r = len(nums)-1 # 5

            while l<r:
                currsum = nums[i]+nums[l]+nums[r]
                if currsum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1     # why do we do these 2
                    r-=1     #
                    while nums[l]==nums[l-1] and l<r: # make sure this line makes sense fully
                        l+=1
                elif currsum<0:
                    l+=1
                else:
                    r-=1
        return res
