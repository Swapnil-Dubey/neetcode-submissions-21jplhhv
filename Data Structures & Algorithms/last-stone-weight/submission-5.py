class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones)>1:
            max1 = heapq.heappop_max(stones)
            max2 = heapq.heappop_max(stones)

            if max1<max2: 
                heapq.heappush_max(stones, max2-max1)
            elif max2<max1:
                heapq.heappush_max(stones, max1-max2)
        return stones[0] if stones else 0