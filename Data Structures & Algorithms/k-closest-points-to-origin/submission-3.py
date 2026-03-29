class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []
        heapq.heapify(dists)
        res = []
        
        for (x,y) in points:
            dist = (x**2)+(y**2)
            heapq.heappush(dists, (dist,x,y))
        
        for i in range(k):
            res.append(heapq.heappop(dists)[1:])

        return res