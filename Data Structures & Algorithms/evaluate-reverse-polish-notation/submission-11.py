class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #input = str [] tokens
        #output = int result of rpn
        #constraints = tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].
        #edge cases = empty array, division by 0, Assume that division between integers always truncates toward zero.
        #pattern and approach = stack because applying operation to last 2 seen integers then popping it and appending the result to the stack
        #time complexity = O(n)
        #space complexity = O(n)

        stack = []

        for s in tokens:
            if s == "+":
                latest = stack.pop()
                second = stack.pop()
                stack.append(latest+second)
            elif s== "-":
                latest = stack.pop()
                second = stack.pop()
                stack.append(second-latest)
            elif s == "*":
                latest = stack.pop()
                second = stack.pop()
                stack.append(second*latest)
            elif s == "/":
                latest = stack.pop()
                second = stack.pop()
                stack.append(int(second/latest))#to truncate towards 0, use int(). To truncate towards negative infinity use /.
            else:
                stack.append(int(s))
        return stack[0]
        