class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i == "+":
                last = stack.pop()
                secondlast = stack.pop()
                stack.append(last+secondlast)
            elif i == "-":
                last = stack.pop()
                secondlast = stack.pop()
                stack.append(secondlast-last)
            elif i == "*":
                last = stack.pop()
                secondlast = stack.pop()
                stack.append(last*secondlast)
            elif i == "/":
                last = stack.pop()
                secondlast = stack.pop()
                stack.append(int(secondlast/last))
            else:
                stack.append(int(i))
        return stack[0]

                