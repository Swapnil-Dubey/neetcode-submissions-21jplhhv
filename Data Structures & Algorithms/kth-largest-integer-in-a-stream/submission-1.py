class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap) #minheap even though we are looking for kth largest
        #       because we want the root of the heap to be the kth largest (not the largest) element in the
        #       sequence, so we use min heap of size k which holds the biggest elements seen so far, anything
        #       smaller gets kicked out. So the smallest survivor(the root) is exactly the kth largest
        while len(self.minheap)>k:
            heapq.heappop(self.minheap)

            #we essentially keep only the k largest elements in the heap because of heap size
            #and this while loop which pops out the smallest elements in the heap until only k remain
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)

        if len(self.minheap)>self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
