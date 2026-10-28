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
        if head is None: return None
        
        # Add new nodes as next pointer
        curr = head
        while curr:
            cp = Node(x=curr.val)
            cp.next = curr.next
            curr.next = cp
            curr = cp.next
        
        newHead = head.next

        # Populate random values
        curr = head
        while curr and curr.next:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # Assign next and split up list
        curr = head
        while curr and curr.next:
            cp = curr.next
            curr.next = cp.next
            if cp.next is not None:
                cp.next = cp.next.next
            curr = curr.next

        return newHead

