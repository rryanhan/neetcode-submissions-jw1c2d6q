class Node:
    def __init__(self, key, value):
        # key will be used for the hasmap, necessary for o(1) time.
        # value we need as the returning value
        self.key, self.val = key, value
        self.prev, self.next = None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        # make dummy nodes
        self.right = Node(0, 0) # MRU
        self.left = Node(0, 0) # LRU
        self.right.prev = self.left
        self.left.next = self.right
        
    def remove(self, node):
         # set prev.next to node.next
         # set next.prev to node.prev
         prev, nxt = node.prev, node.next
         prev.next, nxt.prev = nxt, prev
         # 1 <-> 2 <-> 3


    def insert(self, node):
        # set as MRU, put before right.prev
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        nxt.prev = node
        node.next = nxt
        # 1 <-> 2 <-> 3 <-> R

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
