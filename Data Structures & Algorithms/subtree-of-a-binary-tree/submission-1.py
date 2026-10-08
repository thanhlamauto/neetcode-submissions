# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    from collections import deque
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(root1, root2):
            queue = deque([(root1, root2)])

            while queue:
                node1, node2 = queue.popleft()

                if not node1 and not node2:
                    continue
                if not node1 or not node2:
                    return False
                if node1.val != node2.val:
                    return False

                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            
            return True
        queue2 = deque([root])

        while queue2:
            node = queue2.popleft()
            if node.val == subRoot.val:
                if check(node, subRoot):
                    return True
            if node.left:
                queue2.append(node.left)
            if node.right:
                queue2.append(node.right)
        return False