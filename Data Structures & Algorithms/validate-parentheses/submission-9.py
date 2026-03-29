class Solution:
    def isValid(self, s: str) -> bool:
        # input = string s
        # output = boolean (true if s is valid)
        # notes: s can only be brackets
        #        s is valid iff: open bracket is closed, 
        #        open bracket closed in correct order,
        #        close bracket has corresponding open bracket

        stack = []
        closetoopen = {"}":"{","]":"[",")":"("}

        for c in s:
            if c in closetoopen.values():
                stack.append(c)
            else:
                if len(stack)==0:
                    return False
                elif stack[-1]!=closetoopen[c]:
                    return False
                else:
                    stack.pop()
                
        if len(stack)!=0:
            return False
        return True
        