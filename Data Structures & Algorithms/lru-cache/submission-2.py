class Node:
    def __init__(self,key,value):
        self.key = key
        self.val= value
        self.prev = None
        self.next = None

class LRUCache:
    #fixed capacity cache

    #trick: hashmap (key to value) where value is a pointer to Node<Key,Value> DLL
    #       left (LRU) pointer, right (MRU) pointer

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}#map key to pointer to node

        self.left = Node(0,0) #LRU
        self.right = Node(0,0) #MRU

        self.left.next = self.right #initially they are connected to each other
        self.right.prev = self.left
        
# remove any node from the list
    def remove(self,node):
        prev,next = node.prev, node.next
        prev.next = next
        next.prev = prev

#insert at rightmost position in the list
    def insert(self,node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node



    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

        
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            self.cache.pop(self.left.next.key)
            self.remove(self.left.next)
            

        
