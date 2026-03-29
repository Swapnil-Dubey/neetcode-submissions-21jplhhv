class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            currmin = val
        elif val<self.stack[-1][1]:
            currmin = val
        else:
            currmin = self.stack[-1][-1]
        self.stack.append((val,currmin))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
