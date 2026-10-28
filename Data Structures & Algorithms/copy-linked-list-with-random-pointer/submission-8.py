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
        # add copy node between curr and next
        if head is None: return None

        curr = head
        while curr is not None:
            copy = Node(curr.val)
            copy.next = curr.next
            curr.next = copy

            curr = copy.next

        copyHead = head.next

        # assign each new node their random copy
        curr = head
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            
            curr = curr.next.next

        # assign each new node their next copy
        curr = head
        while curr is not None:
            copy = curr.next
            curr.next = copy.next
            if copy.next is not None:
                copy.next = copy.next.next
            
            curr = curr.next

        return copyHead
