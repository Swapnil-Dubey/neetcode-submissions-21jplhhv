class Node:

    def __init__(self, key:int, val: int):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #key:pointertonode

        self.left = Node(0,0)
        self.right = Node(0,0)

        #dummy nodes: left = LRU, right = MRU
        self.left.next = self.right
        self.right.prev = self.left

    #remove from list
    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev
    
    #insert at right
    def insert(self, node):
        prev = self.right.prev
        self.right.prev = node
        node.next = self.right
        node.prev = prev
        prev.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

        if len(self.cache)>self.cap:
            #remove from LL and delete the LRU from the cache:
            lrunode = self.left.next
            self.remove(lrunode)
            del self.cache[lrunode.key]
        


