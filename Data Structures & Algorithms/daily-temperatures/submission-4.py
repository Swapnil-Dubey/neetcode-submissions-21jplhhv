class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)

        stack = []

        for i in range(len(temperatures)):
            while len(stack)!=0 and stack[-1][0]<temperatures[i]:
                removed = stack.pop()
                res[removed[1]]=i-removed[1]
            stack.append((temperatures[i],i))

        return res