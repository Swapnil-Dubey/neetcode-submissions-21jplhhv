class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        freqmap = [[] for _ in range(len(nums)+1)] 
        count = {}

        for i in nums:
            if i in count:
                count[i]+=1
            else:
                count[i]=1 

        

        for x in count: 
            freqmap[count[x]].append(x)
        

        for y in range(len(freqmap)-1,0,-1):
            if k!=0:
                for x in range(len(freqmap[y])-1,-1,-1):
                    ret.append(freqmap[y][x])
                    freqmap[y].pop()
                    k-=1
        return ret

