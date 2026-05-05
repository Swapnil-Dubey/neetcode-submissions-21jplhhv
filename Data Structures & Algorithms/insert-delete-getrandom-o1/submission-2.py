class RandomizedSet:
    import random
    def __init__(self):
        self.hashmap = {} #val to index in arr mapping
        self.arr = []
    


    def insert(self, val: int) -> bool:
        if val in self.hashmap:
            return False
        self.arr.append(val)
        self.hashmap[val] = len(self.arr)-1
        return True
        

    def remove(self, val: int) -> bool:
        if val in self.hashmap:
            self.arr[self.hashmap[val]] = self.arr[-1]
            self.hashmap[self.arr[self.hashmap[val]]] = self.hashmap[val]
            self.arr.pop()
            self.hashmap.pop(val)
            return True
        else: 
            return False

    def getRandom(self) -> int:
        return random.choice(self.arr)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()