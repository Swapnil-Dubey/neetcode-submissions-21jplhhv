class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #input = [int]
        #output = subarray of max product

        #edge case: single element, negatives, 0s

        #maintain maxproduct subarray, minproduct subarray so far adn keep adding elements to the sub araray, 0 resets maxproductsub to 1, and also minproductsub to 1


        res = max(nums) #imp

        curMin, curMax = 1,1

        for n in nums:
            if n==0:
                curMin = 1
                curMax = 1
                continue
            temp = curMax*n
            curMax = max(n*curMax, n*curMin, n) #imp
            curMin = min(temp, n*curMin, n) #imp
            res = max(res,curMax)
        return res