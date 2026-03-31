# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append([root, -99999, 99999])

        while q:
            node, lower, upper = q.popleft()
            if lower < node.val < upper:
                if node.left:
                    q.append([node.left, lower, node.val])
                if node.right:
                    q.append([node.right, node.val, upper])
            else:
                return False
        return True

        

#             2
#.    1              5
#
# 0       10      3        20
#
