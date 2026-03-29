class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k <= number of distinct elements in nums
        #freq (index) to list of elements array

        #k max is number of distinct elements in nums and max of that is total number of elements in the array

        seen = [[] for _ in range(len(nums)+1)]
        dseen = {}

        for i in nums:
            if i in dseen:
                dseen[i]+=1
            else:
                dseen[i]=1
        

        for i in dseen:
            seen[dseen[i]].append(i)

        x = len(seen)
        
        res = []

        while k>0:
            if len(seen[x-1])!=0:
                res.append(seen[x-1][-1])
                seen[x-1].pop()
                k-=1
            else:
                x-=1

        return res