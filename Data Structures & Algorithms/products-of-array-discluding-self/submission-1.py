class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        for i in range(len(nums)):
            if i != 0:
                prefix.append(prefix[i-1]*nums[i-1])
            else:
                prefix.append(1)

        for i in range(len(nums)-1, -1, -1):
            if i != len(nums)-1:
                postfix.insert(0, postfix[0]*nums[i+1])
            else:
                postfix.append(1)
        returnlist = []
        for i in range(len(prefix)):
            returnlist.append(prefix[i]*postfix[i])
        return returnlist


