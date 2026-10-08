# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stackp = deque([p])
        stackq = deque([q])
        while stackp and stackq:
            nodep = stackp.popleft()
            nodeq = stackq.popleft()

            if nodep:
                if nodeq:
                    if (nodep.val != nodeq.val):
                        return False
                    stackq.append(nodeq.left)
                    stackq.append(nodeq.right)
                else:
                    return False
                stackp.append(nodep.left)
                stackp.append(nodep.right)
            else:
                if nodeq:
                    return False


            # if nodep and nodeq:
            #     if (nodep.val != nodeq.val):
            #         return False
            # else:
            #     if (nodep == None and nodeq != None) or (nodeq == None and nodep != None):
            #         return False
            # stackp.append(nodep.right)

            # stackp.append(nodep.left)

            # stackq.append(nodeq.right)

            # stackq.append(nodeq.left)
        if len(stackp) > 0 or len(stackq) > 0:
            return False
        return True
            