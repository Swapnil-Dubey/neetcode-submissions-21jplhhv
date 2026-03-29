class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    #edge cases: 1 length temperatures array
    #pattern: stack because we are keeping track of temperatures that havent yet seen a warmer temperatures and popping all of them as soon as we encounter a warmer temp than them (2 1 3) is ok bcz it'll be warmer than 2 and also 1 so keep popping
    # approach is that keep a stack of temperatures that havent seen warmer temperature yet (and their index) and pop when u see it and change their value in the res array to curr warmer temp index - their index 
    #time complexity: O(n)
    # space = O(n)


        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if i == 0:
                stack.append([i,temperatures[i]])
            else:
                while stack and stack[-1][1]<temperatures[i]:
                    popped = stack.pop()
                    res[popped[0]] = i-popped[0]
                stack.append([i,temperatures[i]])
        return res


