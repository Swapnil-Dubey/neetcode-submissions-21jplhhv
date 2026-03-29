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
                stack.append(int(secondlast/last)) #####impppp    int() typecasting on floats rounds towrds 0 (+ve and negative numbers both)
            elif n =="*":
                last= stack.pop()
                secondlast = stack.pop()
                stack.append(last*secondlast)
            else:
                stack.append(int(n))###
        return stack[0]