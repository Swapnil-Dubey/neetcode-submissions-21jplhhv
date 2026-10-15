class Solution:
    def isValid(self, s:str)->bool:
        #empty string?
        # stack

        stack = []

        closetoopen = {"]":"[","}":"{",")":"("}

        for c in s:
            if c in closetoopen:
                if stack and closetoopen[c] != stack[-1]:####
                    return False 
                else:
                    if stack:
                        stack.pop()#####
                    else:
                        return False
            else:
                stack.append(c)
        return len(stack)==0####

