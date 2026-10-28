class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.addToFront(node)
            return node.val
        return -1

    def removeNode(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def addToFront(self, node):
        prev, nxt = self.head, self.head.next
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.addToFront(node)
        
        if len(self.cache) > self.capacity:
            removed = self.tail.prev
            self.removeNode(removed)
            del self.cache[removed.key]
        
