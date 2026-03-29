class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # input = [int]
        # output = [int]

        res = [0]*len(temperatures)
                    # why stack? how to recognize stack?
        stack = []

        for n in range(len(temperatures)):
            if len(stack)==0:
                stack.append((temperatures[n],n))
            else:
                i = len(stack)-1
                while i>-1:
                    if stack[i][0]<temperatures[n]:
                        popped = stack.pop()
                        res[popped[1]]=n-popped[1]
                    i-=1
                stack.append((temperatures[n],n))
        return res