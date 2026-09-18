# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def depth(node):
            nonlocal res 

            if not node:
                return 0

            left_depth = depth(node.left)
            right_depth = depth(node.right)

            res = max(res, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)
        
        depth(root)
        return res