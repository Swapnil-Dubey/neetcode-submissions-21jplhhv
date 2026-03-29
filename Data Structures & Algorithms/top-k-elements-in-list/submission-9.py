class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #[] index is count, element is list of elements of nums with that count
        res = []
        tracker = [[] for _ in range(len(nums)+1)] #[[],[],[],[]]
        freq = {}
        for i in nums: 
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1 #{1:1,2:2,3:3}

        for i in freq:
            tracker[freq[i]].append(i) # [[],[1],[2],[3]]
        

        for i in range(len(tracker)-1,-1,-1): # 2 1 0
            if k>0:
                res+=tracker[i]
                k-=len(tracker[i])
        
        return res


        