class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #minheap so we can take out the min freq value every time
        #maintian a k length minheap

        heap = []
        heapq.heapify(heap)

        #{element:count}
        seen = {}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i] = 1

        for i in seen:
            heapq.heappush(heap,(seen[i],i))
            if len(heap)>k:
                heapq.heappop(heap)
        
        return list(map(lambda x:x[1], heap))

        