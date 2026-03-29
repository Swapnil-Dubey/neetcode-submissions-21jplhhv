class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # input = array of ints
        #we're keeping stack in decreasing order and pop the latest one 

        stack = []
        res = [0]*len(temperatures)

        for i in range(len(temperatures)):
            if len(stack)==0:
                stack.append((i,temperatures[i]))
            else:
                while stack and temperatures[i]>stack[-1][1]:
                    popped = stack.pop()
                    res[popped[0]]=i-popped[0]
                stack.append((i,temperatures[i]))
        return res