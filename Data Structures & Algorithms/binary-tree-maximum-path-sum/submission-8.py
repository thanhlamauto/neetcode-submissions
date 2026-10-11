# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(node):
            nonlocal max_sum

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            path_through = max(node.val + left, node.val + right, node.val + left + right, node.val)

            max_sum = max(path_through, max_sum)

            return max(node.val + left, node.val + right, node.val)
        
        dfs(root)
        return max_sum

        