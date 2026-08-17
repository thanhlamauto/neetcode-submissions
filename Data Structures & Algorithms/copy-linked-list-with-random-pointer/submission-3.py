class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        cur = head

        # Pass 1: copy tất cả node
        while cur:
            old_to_new[cur] = Node(cur.val)
            cur = cur.next

        cur = head

        # Pass 2: nối next và random
        while cur:
            copy = old_to_new[cur]

            copy.next = old_to_new.get(cur.next)
            copy.random = old_to_new.get(cur.random)

            cur = cur.next

        return old_to_new[head]