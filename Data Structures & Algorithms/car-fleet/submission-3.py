class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #input = [int] position, [int] speed, int target
        #output = int carfleets

        #same direction travelling, no car can pass another, instead catchup and go at same speed
        # if catchup at target position even then consider as same fleet

        # pattern = stack because we pop the cars that form a fleet with ith car
        #approach = t = d/s if t of cars that are behind is less than cars at front, they will form a fleet

        stack = []
        for (p,s) in sorted(list(zip(position,speed))):
            print(p,s)
            print((target-p)/s)
            while stack and (target-p)/s >= stack[-1]: #imp dont forget if you're looping popping while stack**
                stack.pop()
            stack.append((target-p)/s)
        return len(stack)