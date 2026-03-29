class Solution:
    def isValid(self, s: str) -> bool:
        lastseenopenbracket = []
        opens = ["(","{","["]
        openclose = {")":"(", "}":"{", "]":"["}
        for c in s:
            if c in opens:
                lastseenopenbracket.append(c)
            else:
                if len(lastseenopenbracket) == 0:
                    return False
                else:
                    if lastseenopenbracket[-1] == openclose[c]:
                        lastseenopenbracket.pop()
                    else:
                        return False
        if len(lastseenopenbracket)==0:
            return True
        else:
            return False



        