class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distp = []
        for p in points:
            dist = (p[0]**2)+(p[1]**2)
            distp.append((dist,p))
        
        heapq.heapify(distp)
        res = []
        for i in range(k):
            todo = heapq.heappop(distp)
            res.append(todo[1])
        return res
