class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closd = {")":"(","]":"[","}":"{"}
        for c in s:
            if c in closd.keys():
                if len(stack) == 0:
                    return False
                elif stack[-1] == closd[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack)==0:
            return True
        return False