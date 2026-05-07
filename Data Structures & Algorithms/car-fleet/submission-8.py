class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #dest is at position target miles

        #maintain a monotonic stack of t = d/s

        # if u see a t that is less than t's in the stack. remove them while loop

        pair = [(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse = True)

        stack = [] 

        for p,s in pair:
            t_curr = (target-p)/s
 
            if stack and stack[-1]>=t_curr:
                continue
            stack.append(t_curr)
        return len(stack)

