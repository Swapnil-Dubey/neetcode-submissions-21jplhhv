class DynamicArray:

    def __init__(self, capacity: int):
        self.l = list()
        self.capacity = capacity


    def get(self, i: int) -> int:
        if i>=0 and i<self.getSize():
            return self.l[i]

    def set(self, i: int, n: int) -> None:
        if i>=0 and i<self.capacity:
            self.l[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize()<self.capacity:
            self.l.append(n)
        else:
            self.resize()
            self.pushback(n)

    def popback(self) -> int:
        if self.getSize()>0:
            return self.l.pop()

    def resize(self) -> None:
        self.capacity*=2

    def getSize(self) -> int:
        return len(self.l)
    
    def getCapacity(self) -> int:
        return self.capacity