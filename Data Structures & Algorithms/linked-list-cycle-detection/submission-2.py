# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # visited = set()
        # while head:
        #     if head in visited:
        #         return True
        #     visited.add(head)
        #     head = head.next
        # return False

        slow = head
        fast = head

        while slow and fast:
            t = 0
            while t < 2:
                fast = fast.next
                if not fast:
                    return False
                t += 1
            slow = slow.next
            if slow == fast:
                return True
        return False

