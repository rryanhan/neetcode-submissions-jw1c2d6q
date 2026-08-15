class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev 

    def insert(self, node):
        mru = self.right.prev
        mru.next, node.prev = node, mru
        node.next, self.right.prev = self.right, node
        

    def get(self, key: int) -> int:
        # if key in cache, pull from cache
        # then, remove from LL
        # put at the rightmost side
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1
        

    def put(self, key: int, value: int) -> None:
        # if key in cache, update the key value, remove from LL, insert at rightmpst
        # if not, put in cache, insert at rightmost
        if key in self.cache:
            self.remove(self.cache[key])
            
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(self.cache[lru.key])
            del self.cache[lru.key]

        
