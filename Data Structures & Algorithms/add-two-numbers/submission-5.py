# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr = head = ListNode()

        while l1 or l2 or carry:
            total = carry
            
            if l1 is not None:
                total += l1.val
                l1 = l1.next
            
            if l2 is not None:
                total += l2.val
                l2 = l2.next

            curr.next = ListNode(total % 10)
            carry = total // 10

            curr = curr.next

        return head.next
