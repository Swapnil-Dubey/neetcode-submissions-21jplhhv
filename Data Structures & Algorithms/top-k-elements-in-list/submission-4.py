class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for e in nums:
            if e in d:
                d[e]+=1
            else:
                d[e]=1
        numcount = list(d.items())
        sortednumcount = sorted(numcount, key = lambda x:x[1], reverse = True)

        
        return list(map(self.returnfirst,list(sortednumcount[:k])))
    def returnfirst(self,t):
        return t[0]
