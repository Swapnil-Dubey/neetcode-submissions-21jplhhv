class Solution:
    def isValid(self, s: str) -> bool:
        seenopenstack = []
        open = {'(':')','{':'}','[':']'}

        for i in s:
            if i in open:
                seenopenstack.append(i)
            else:
                if len(seenopenstack) == 0:
                    return False
                if i == open[seenopenstack[-1]]:
                    seenopenstack.pop()
                else:
                    return False
        if len(seenopenstack) == 0:
            return True
        return False