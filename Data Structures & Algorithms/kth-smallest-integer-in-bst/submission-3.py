# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        res = None

        def dfs(node):
            nonlocal count
            nonlocal res
            if not node:
                return
            if res is not None:
                return
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
                return
            dfs(node.right)
            return
            
        dfs(root)
        
        return res

            
