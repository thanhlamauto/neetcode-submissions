# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(node, low, high):
            if node is None:
                return True
            
            if node.val >= high or node.val <= low:
                return False

            return check(node.left, low, node.val) and check(node.right, node.val, high)
        
        low = float('-inf')
        high = float('inf')
        return check(root, low, high)

        
        

        
