class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #products of all elements upto but excluding ith
        left = [1]*len(nums)

        for i in range(len(nums)):
            if i != 0:
                left[i] = left[i-1]*nums[i-1]
        



        #products of all elements upto but excluding ith (starting from the right)
        right = [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            if i != len(nums)-1:
                right[i] = right[i+1]*nums[i+1]
        


        output = [1]*len(nums)

        for i in range(len(nums)):
            output[i]=left[i]*right[i]
        return output
        