class Solution:
    def checkValidString(self, s: str) -> bool:
        open = []
        star = []
        i = 0


        for c in s:
            
            if c == ")":
                if open:
                    open.pop()
                elif star:
                    star.pop()
                else:
                    return False
            elif c == "(":
                open.append(i)
            else:
                star.append(i)
            
            i+=1

        
        while open and star:
            if open.pop()>star.pop():
                return False
            
        return not open



    




    # in what conditions should we treat * as ( or ) or ""
    #   if stack has ( then treat it as )
    #   if stack is empty then treat it as ""
