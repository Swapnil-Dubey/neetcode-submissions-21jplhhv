class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #solution exists only if sum(gas)>=sum(cost)
        

        diff = []
        res = 0

        for i in range(len(gas)):
            diff.append(gas[i]-cost[i])
        
        if sum(diff)<0:
            return -1
        
        total = 0
        
        for i in range(len(diff)):
            total+=diff[i]
            if total<0:
                total = 0
                res = i+1
        return res
            

            #at the end of arr positive sum of gas == total
            
            
            
            


