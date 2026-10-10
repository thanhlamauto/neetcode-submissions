# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []

        def dfs(node):
            nonlocal order
            if not node:
                return
            dfs(node.left)
            order.append(node.val)
            dfs(node.right)
            return
            
        dfs(root)
        
        return order[k-1]

            
