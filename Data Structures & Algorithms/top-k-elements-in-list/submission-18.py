class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #max heap


        seen = []
        heapq.heapify_max(seen)

        seendict = {}

        for i in nums:
            if i in seendict:
                seendict[i]+=1
            else:
                seendict[i] = 1
        for el in seendict:
            heapq.heappush_max(seen,(seendict[el], el))
        res = []
        for i in range(k):
            res.append(heapq.heappop_max(seen)[1])
        return res

