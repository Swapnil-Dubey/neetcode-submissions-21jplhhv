class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countdict = {}
        for i in nums:
            if i in countdict:
                countdict[i]+=1
            else:
                countdict[i]=1
        # now we have {1:1, 2:2, 3:3}
        # we need to sort in reverse order by values

        countdict_sorted = dict(sorted(countdict.items(), key=lambda item: item[1], reverse=True))

        return list(countdict_sorted.keys())[0:k]

