class Solution:
    def isValid(self, s: str) -> bool:
        #input = string s consisting of brackers
        #output = true if s is valid

        #edge cases: s len == 1
        



        # try to catch for wrongs as we iterate through the string

        stack = []
        opentoclose = {'(':')','[':']','{':'}'}

        for c in s:
            if c in opentoclose:
                stack.append(c)
            else:
                if stack and opentoclose[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
