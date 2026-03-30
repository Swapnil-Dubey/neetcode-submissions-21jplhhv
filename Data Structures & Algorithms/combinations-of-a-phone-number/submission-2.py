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

        curr =""
        
        def dfs(i):
            nonlocal curr
            if i == len(digits):
                res.append(curr)
                return
            for s in digitToChar[digits[i]]:
                curr+=s
                dfs(i+1)
                curr = curr[:-1]
        dfs(0)
        if res[0] == "":
            return []
        else:
            return res