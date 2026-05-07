class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #dest is at position target miles

        #maintain a monotonic stack of t = d/s

        #sorted in position reverse = True
        #   if a car came after a prev car (position is less than position of prev car)
        #   and its time to reach dest < time for prev car to reach dest
        #   then they became a fleet

        


        stack = [] 

        for p,s in sorted(zip(position,speed), reverse = True):
            t_curr = (target-p)/s
 
            if stack and stack[-1]>=t_curr:
                continue
            stack.append(t_curr)
        return len(stack)

