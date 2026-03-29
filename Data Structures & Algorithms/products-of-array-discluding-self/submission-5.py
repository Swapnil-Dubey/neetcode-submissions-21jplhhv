class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lrproduct = [1]*len(nums)
        rlproduct = [1]*len(nums)

        #input = [int]
        #output = [int]
                #output[i] = product of all elements of nums except nums[i] so -> lrproducts[i]*rlproducts[i]

        #edge cases: empty list

        for i in range(len(nums)):
            if i==0:
                lrproduct[i]=1
            else:
                lrproduct[i]=lrproduct[i-1]*nums[i-1]
        
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                rlproduct[i]=1
            else:
                rlproduct[i]=rlproduct[i+1]*nums[i+1]
        
        result = [1]*len(nums)

        for i in range(len(result)):
            result[i]=lrproduct[i]*rlproduct[i]
        
        return result

            



