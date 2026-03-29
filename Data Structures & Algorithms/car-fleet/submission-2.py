class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for (p,s) in sorted(list(zip(position,speed)))[::-1]:
            print(p,s)
            if len(stack)==0:
                stack.append((target-p)/s)
                print("stack: ", stack)
            else:
                if (target-p)/s<=stack[-1]:
                    continue
                else:
                    stack.append((target-p)/s)
        return len(stack)

