class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #input = array of int
        #output: weight of last remaining stone or 0 if none remain
        #constraints: 1 <= stones.length <= 20
#                       1 <= stones[i] <= 100
#                       continue smashing until no more than 1 stone remains
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x==y:
                continue
            elif x<y:
                heapq.heappush(stones, x-y)
            else:
                heapq.heappush(stones, y-x)
        return abs(stones[0]) if stones else 0

