class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftprod = [1]*len(nums)
        rightprod = [1]*len(nums)

        prodsofar = 1
        for i in range(len(nums)):
            if i!=0:
                leftprod[i] = nums[i-1]*prodsofar
                prodsofar = leftprod[i]
        prodsofar = 1 
        for i in range(len(nums)-1,-1,-1):
            if i!=len(nums)-1:
                rightprod[i] = nums[i+1]*prodsofar
                prodsofar = rightprod[i]
        

        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i] = leftprod[i]*rightprod[i]


        return res

        