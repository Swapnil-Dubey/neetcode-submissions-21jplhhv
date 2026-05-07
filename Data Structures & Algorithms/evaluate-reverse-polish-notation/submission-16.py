class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #recognize that this is a stack problem(we stack 2 integers and pop,process,restack them when we encounter an operation)
        stack = []

        for token in tokens:
            if token == '+':
                first = stack.pop()
                last = stack.pop()
                stack.append(first+last)
            elif token == "*":
                first = stack.pop()
                last = stack.pop()
                stack.append(first*last)
            elif token == "-":
                first = stack.pop()
                last = stack.pop()
                stack.append(last-first)
            elif token == "/":
                first = stack.pop()
                last = stack.pop()


                stack.append(int(last/first))
            else:
                stack.append(int(token))
        return stack[0]