class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # k is bounded by number of distinct elements in array => max = len(nums)
        #so our index can be frequency which is k (bounded by len(nums)) and element can be list of elements in nums that appear that
        # many times in the array



        seen = {}
        for n in nums:
            if n in seen:
                seen[n]+=1
            else:
                seen[n] = 1
        # now we have a dict of num:freq

        l = [[] for _ in range(len(nums)+1)]#+1 for 0 freq (1 based indexing)
        

        for el in seen:
            l[seen[el]].append(el)


        res = []

        i = len(l)-1

        while k>0:
            if len(l[i])>0:
                res.append(l[i][-1])
                k-=1
                l[i].pop()
            else:
                i-=1
        return res



