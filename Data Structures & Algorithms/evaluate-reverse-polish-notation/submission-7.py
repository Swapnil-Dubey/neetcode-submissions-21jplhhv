class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n == "+":
                last=stack.pop()
                secondlast=stack.pop()

                stack.append(last+secondlast)
            elif n=="-":
                last=stack.pop()
                secondlast=stack.pop()
                stack.append(secondlast-last)

            elif n == "*":
                last=stack.pop()
                secondlast=stack.pop()
                stack.append(secondlast*last)

            elif n =="/":
                last=stack.pop()
                secondlast=stack.pop()
                stack.append(int(secondlast/last))
            else:
                stack.append(int(n))
        return stack[0]