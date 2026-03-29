class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #first element of nums gets inserted at each position in the permutations of the sub problem (nums except 1st element)
        res = []

        if len(nums)==0:
            return [[]]
        

        perms = self.permute(nums[1:])

        for p in perms:
            for c in range(len(p)+1):
                pcopy = p.copy()
                pcopy.insert(c, nums[0])
                res.append(pcopy)
        return res


        