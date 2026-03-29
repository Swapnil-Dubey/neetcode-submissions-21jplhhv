class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #input = int [] temperatures
        #output = int [] result
        #           result[i] = number of days after ith day before a warmer temp, otherwise 0

        result = [0]*len(temperatures)

        #edge cases: 1 element temperatures list
        #pattern: Stack (because a new higher element pops all the lower temp elements recently added
            # to the stack and then add onto the stack)
        #time complexity: O(n)
        #space complexity: O(n)

        stack = []

        for t in range(len(temperatures)):
            while stack and stack[-1][0]<temperatures[t]:
                popped = stack.pop()
                result[popped[1]]=t-popped[1]
            stack.append((temperatures[t],t))
        return result
