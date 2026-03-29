class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []#list of tuples (distto00,[point])

        for p in points:
            dist = (p[0]**2 + p[1]**2)
            dists.append((dist,p))
        
        heapq.heapify(dists)
        res = []

        for i in range(k):
            res.append(heapq.heappop(dists)[1])

        return res
        