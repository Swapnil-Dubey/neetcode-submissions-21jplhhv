class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # 2 can be in:
        #1,2,3
        #2,3,4



        # min val avl to us here = 1 (x)
        # and min val can only be in 1 possible group: [1 (x),...n] where n = groupSize


        #early check len(hand)//groupSize == 0

        if len(hand)%groupSize!=0:
            return False
        
        #get the lowest freq val from minheap, try to form consecutive seq starting at that value
        #   if u cant then return false
        #   if u can then make freq of each val in this sequence formed -=1 and if freq is 0 at any point then remove min val from minheap ONLY if it matches, otherwise return #false.


        #hashmap (val:freq)
        #minheap = [val]
        hashmap = dict()

        for i in hand:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i] = 1
            #heapq.heappush(minheap,i) #imppp this makes it hold duplicates
        minheap = list(hashmap.keys())
        heapq.heapify(minheap)

        while minheap:
            minval = minheap[0]
            curr = minval
            hashmap[curr]-=1
            if hashmap[minval]==0:
                heapq.heappop(minheap)

            for i in range(1,groupSize):
                        
                if curr+1 in hashmap:
                    if hashmap[curr+1]>0:
                        hashmap[curr+1]-=1
                        if hashmap[curr+1]==0:
                            if curr+1!=minheap[0]:
                                return False
                            else:
                                heapq.heappop(minheap)
                        curr+=1
                    else:
                        return False
                else:
                    return False


        return True
                    

        
            



        