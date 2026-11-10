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
        maps = collections.defaultdict(lambda : Node(0))
        maps[None] = None

        curr = head
        while curr:
            maps[curr].val = curr.val
            maps[curr].next = maps[curr.next]
            maps[curr].random = maps[curr.random]
            curr = curr.next

        return maps[head]