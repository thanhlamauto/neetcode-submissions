class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        original_head = head

        copy_head = Node(head.val)
        copy_cur = copy_head

        hmap = {}
        hmap[head] = copy_head

        # Tạo các node copy + next
        while head:
            if head.next:
                next_copy = Node(head.next.val)
                hmap[head.next] = next_copy
            else:
                next_copy = None

            copy_cur.next = next_copy

            copy_cur = copy_cur.next
            head = head.next

        # Gán random
        original_cur = original_head
        copy_cur = copy_head

        while original_cur:
            if original_cur.random:
                copy_cur.random = hmap[original_cur.random]
            else:
                copy_cur.random = None

            original_cur = original_cur.next
            copy_cur = copy_cur.next

        return copy_head