# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2

        if (curr1 and curr2 and curr1.val < curr2.val) or (curr1 and not curr2):
            merge = ListNode(val = curr1.val)
            curr1 = curr1.next
            head = merge
        elif (curr1 and curr2 and curr1.val >= curr2.val) or (curr2 and not curr1):
            merge = ListNode(val = curr2.val)
            curr2 = curr2.next
            head = merge
        else:
            head = curr1

        while curr1 and curr2:
            if curr1.val < curr2.val:
                merge.next = curr1
                curr1 = curr1.next
            else:
                merge.next = curr2
                curr2 = curr2.next
            merge = merge.next
        
        while curr1:
            merge.next = curr1
            curr1 = curr1.next
            merge = merge.next
        
        while curr2:
            merge.next = curr2
            curr2 = curr2.next
            merge = merge.next

        return head

            