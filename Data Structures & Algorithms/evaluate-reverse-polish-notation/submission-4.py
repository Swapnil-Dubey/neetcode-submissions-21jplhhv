class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == "+":
                last= stack.pop()
                secondlast = stack.pop()
                stack.append(last+secondlast)
            elif n=="-":
                last= stack.pop()
                secondlast = stack.pop()
                stack.append(secondlast-last)
            elif n =="/":
                last= stack.pop()
                secondlast = stack.pop()
                if last>0 and secondlast>=0:
                    stack.append(secondlast//last) #how to make this round to 0
                else:
                    stack.append(int(secondlast/last))
            elif n =="*":
                last= stack.pop()
                secondlast = stack.pop()
                stack.append(last*secondlast)
            else:
                stack.append(int(n))###
        return stack[0]