class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #pattern: Stack because each element in a stack is the furthest position vehicle (leader of the fleet), len stack is number of fleets at dest
        #approach: sort zip position and speed by position, iterate through each position, calculate t = d/s if t for car at p smaller than t for car at p later then the car behind is passing it (reaching in time < t further car) so these 2 become a fleet
        #time complexity: O(n)
        #space complexity: O(n)
        fleet_stack = []
        for (p,s) in sorted(zip(position, speed)):
            t = (target-p)/s
            while fleet_stack and t>=fleet_stack[-1]: # remember t>= here because even if they converge at dest, still considered the same fleet (2 cars at diff pos, but taking the same time to reach teh destination)
                fleet_stack.pop()
            fleet_stack.append(t)
        return len(fleet_stack)
