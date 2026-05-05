class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}

        for c in s:
            if c in freq:
                freq[c]+=1
            else:
                freq[c]=1
        heap = []
        for c in freq:
            heapq.heappush_max(heap,(freq[c],c))
        
        #keep picking the most freq char and joinin into our result string
        res = ""
        while heap:
            c = heapq.heappop_max(heap)
            if len(res)>0 and res[-1]==c[1]:
                try:
                    c_old = c
                    c = heapq.heappop_max(heap)
                    heapq.heappush_max(heap, c_old)
                
                except:
                    return ""
            res+=c[1]
            c = (c[0]-1,c[1])
            if c[0]>0:
                heapq.heappush_max(heap, (c[0],c[1]))
            
        return res

