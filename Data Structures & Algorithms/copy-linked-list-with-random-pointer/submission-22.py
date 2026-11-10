"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        maps = {None: None}

        curr = head
        while curr:
            copy = Node(curr.val)
            maps[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = maps[curr]                    
            copy.next = maps[curr.next]
            copy.random = maps[curr.random]
            curr = curr.next

        return maps[head]