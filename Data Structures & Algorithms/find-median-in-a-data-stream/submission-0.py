class MedianFinder:
    #small heap(maxheap) and large heap (minheap)

    def __init__(self):
        self.small = [] #max heap
        self.large = [] #min heap
        

    def addNum(self, num: int) -> None:
        if self.small and num<self.small[0]:
            heapq.heappush_max(self.small, num)
        else:
            heapq.heappush(self.large, num)


        if len(self.small)-len(self.large)>1:
            heapq.heappush(self.large, heapq.heappop_max(self.small))

        if len(self.large)-len(self.small)>1:
            heapq.heappush_max(self.small, heapq.heappop(self.large))

        

    def findMedian(self) -> float:
        if (len(self.small)+len(self.large))%2==1:
            if len(self.small)>len(self.large):
                
                return self.small[0]
            else:
                
                return self.large[0]
        else:
            return (self.small[0]+self.large[0])/2
        


    