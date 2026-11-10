
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
    
    def add(self, node):
        prev, next = self.tail.prev, self.tail
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.remove(node)
            self.add(node)
            return node.val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.remove(self.dict[key])
            
        
        self.dict[key] = Node(key, value)
        self.add(self.dict[key])
        
        if len(self.dict) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.dict[lru.key]
