# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque([root])
        
        while queue:
            level = []
            queue_copy = deque([])
            while queue:
                node = queue.popleft()
                if node.left:
                    queue_copy.append(node.left)
                if node.right:
                    queue_copy.append(node.right)
                level.append(node.val)
            res.append(level)
            queue = queue_copy
            
        
        return res
