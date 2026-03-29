class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #input = array of int
        #output: weight of last remaining stone or 0 if none remain
        #constraints: 1 <= stones.length <= 20
#                       1 <= stones[i] <= 100
#                       continue smashing until no more than 1 stone remains

        heapq.heapify_max(stones)

        while len(stones)>1:
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)

            if x==y:
                continue
            elif x<y:
                heapq.heappush_max(stones, y-x)
            else:
                heapq.heappush_max(stones, x-y)
        return stones[0] if stones else 0

