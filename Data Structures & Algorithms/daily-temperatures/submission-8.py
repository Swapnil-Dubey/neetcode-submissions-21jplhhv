class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0]*len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i]>stack[-1][0]:
                curr = stack.pop()
                result[curr[1]] = i-curr[1]

            stack.append((temperatures[i],i))
        return result
