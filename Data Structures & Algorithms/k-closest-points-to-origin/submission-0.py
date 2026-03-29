from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #{dist:points[i]}

        heap = []

        for p in points:
            heap.append((p[0]**2+p[1]**2,p))

        heapq.heapify(heap)
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
        

        