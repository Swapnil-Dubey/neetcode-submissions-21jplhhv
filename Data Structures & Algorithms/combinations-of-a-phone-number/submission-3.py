class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, currstr):
            if len(currstr)==len(digits):
                res.append(currstr)
                return
            for c in digitToChar[digits[i]]:
                dfs(i+1,currstr+c)
        dfs(0, '')
        if res[0]=="":
            return []
        return res