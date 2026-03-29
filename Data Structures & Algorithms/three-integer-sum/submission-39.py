class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
#input: int [] nums
#output: [[int i,j,k]] res: arr of triplets that sum to 0
#constraints: i!=j!=k, no duplicate triplets
#edge cases: len(nums)==3
#pattern: 3 <= nums.length <= 1000
#approach: sort first to detect duplicates easily, for loop on eaech number, while loop at each iteration of for loop
#   two sum inside the while loop , keep check on duplicates at each iteration of for loop and one of the numbers of while loop
#time complexity: O(n^2)
#space complexity: O(n^2)

        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if i!=0 and nums[i] == nums[i-1]: # imp check for i!= 0 here
                continue
    
            l = i+1
            r = len(nums)-1

            while l<r:
                curr= nums[i]+nums[l]+nums[r]

                if curr==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1 # have to move both pointers after finding a triplet
                    r-=1

                    while l<r and nums[l]==nums[l-1]: #if numbers inside the while is duplicate, keep moving it
                        l+=1
                elif curr<0: 
                    l+=1
                else:
                    r-=1
                
                

        return res
