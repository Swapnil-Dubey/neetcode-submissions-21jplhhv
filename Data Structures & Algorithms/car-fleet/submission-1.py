class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(list(zip(position,speed)))##
        stack = []
        for (p,s) in ps[::-1]:##
            t = (target-p)/s
            if len(stack)==0:
                stack.append(t) 
            else:
                if t<=stack[-1]:
                    continue
                else:
                    stack.append(t)
        return len(stack)
