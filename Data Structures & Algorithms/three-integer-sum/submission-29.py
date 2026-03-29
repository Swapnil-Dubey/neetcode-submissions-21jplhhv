class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #constraints: i,j,k all distinct, output should not contain duplicate triplets
        #edge cases: no triplets
        #pattern: two pointer
        #approach: 
        #time complexity:O(n^2)

        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]: # imp i>0 remember here otherwise at i=0 this fails
                continue
            l = i+1
            r = len(nums)-1

            while l<r: # l<r here because l cant be r (all distinct triplets)
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1 # dont forget to move after finding triplet
                    r-=1

                    while l<r and nums[l-1] == nums[l]: # only need to do this after finding a triplet
                        l+=1

                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1
                else:
                    l+=1
                
                
        return res

                

