# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = ListNode(next=head)
        prev = second
        count = 0
        while first:
            first = first.next
            count += 1
            if count > n:
                prev = prev.next
        prev.next = prev.next.next
        return second.next