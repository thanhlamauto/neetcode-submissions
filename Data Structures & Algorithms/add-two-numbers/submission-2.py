# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_l1 = l1
        curr_l2 = l2
        head = ListNode()
        curr_res = head
        rem = 0
        while curr_l1 and curr_l2:
            sum = curr_l1.val + curr_l2.val + rem
            mod = sum % 10
            rem = (sum - mod) / 10 
            curr_res.next = ListNode(int(mod))
            curr_res = curr_res.next
            curr_l1 = curr_l1.next
            curr_l2 = curr_l2.next
        
        while curr_l1:
            sum = curr_l1.val + rem
            mod = sum % 10
            rem = (sum - mod) / 10 
            curr_res.next = ListNode(int(mod))
            curr_res = curr_res.next
            curr_l1 = curr_l1.next
        
        while curr_l2:
            sum = curr_l2.val + rem
            mod = sum % 10
            rem = (sum - mod) / 10 
            curr_res.next = ListNode(int(mod))
            curr_res = curr_res.next
            curr_l2 = curr_l2.next
        
        if rem > 0:
            curr_res.next = ListNode(int(rem))
        return head.next
        