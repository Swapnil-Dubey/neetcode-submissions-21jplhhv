class MinStack:

    def __init__(self):
        self.stack = [] #stores (el, currmin)
        

    def push(self, val: int) -> None:
        if len(self.stack)>0:
            currmin = self.stack[-1][-1]
            currmin = min(currmin, val)
            self.stack.append((val,currmin))
        else:
            self.stack.append((val, val))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][-1]
        
