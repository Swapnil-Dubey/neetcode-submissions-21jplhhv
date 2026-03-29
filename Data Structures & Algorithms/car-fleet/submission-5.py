class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #input = int target, int[] position, int speed
        #output = int nfleets
        #constraints = vals of positions are unique
        #pattern and approach = stack because if a car further back reaches in time < cars further up front then it forms a fleet with it and remove off the stsack
        #time complexity
        #space complexity

        stack = []

        for (p,s) in sorted(zip(position,speed)): #remember sorted zip trick
            t = (target-p)/s

            while stack and stack[-1]<=t: # remember the = here bczIf a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.
                stack.pop()
            
            stack.append(t)
        return len(stack)
