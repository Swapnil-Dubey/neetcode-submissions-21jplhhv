class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed = {")":"(","]":"[","}":"{"}

        #stack because open bracket are closed in correct order

        for c in s:
            if c in closed:
                if len(stack)==0:
                    return False
                elif stack[-1]!=closed[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)

        if len(stack)!=0:
            return False
        else:
            return True

                