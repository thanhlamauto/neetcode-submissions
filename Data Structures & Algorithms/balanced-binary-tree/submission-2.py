# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def search(root):
            if not root:
                return 0

            leftcount = search(root.left)
            rightcount = search(root.right)
            if leftcount == -1 or rightcount == -1:
                return -1

            difference = abs(rightcount - leftcount)
            if difference > 1:
                return -1
            return max(leftcount, rightcount) + 1
        
        res = search(root)
        print(res)
        if res == -1:
            return False
        return True