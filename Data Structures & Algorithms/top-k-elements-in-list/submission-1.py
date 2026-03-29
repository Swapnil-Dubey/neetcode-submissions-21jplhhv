class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        searchdict = {}
        for i in nums:
            if i in searchdict:
                searchdict[i]+=1
            else:
                searchdict[i]=1
        searchdict= sorted(searchdict, key=searchdict.get, reverse = True)
        returnlist = []
        for i in range(k):
            returnlist.append(searchdict[i])
        return returnlist
