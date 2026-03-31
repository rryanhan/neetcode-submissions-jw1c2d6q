# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        upperB = 10000000
        lowerB = -10000000

        def dfs(node, upperB, lowerB):
            if not node:
                return True
            if node.val <= lowerB or node.val >= upperB:
                return False
            return dfs(node.right, upperB, max(lowerB, node.val)) and dfs(node.left, min(upperB, node.val), lowerB)
        
        return dfs(root, upperB, lowerB)
        



#                   10      ub: 100000, lb = -100000
#           6               14 lb = 10, ub = 100000
#       4       7       12      18       
#           
#
# if node.left -> is the node smaller than the upper bound?
# if node.right -> if the node greater than the upper bound?
#
# dfs(node, upperB, lowerB)
# start with dfs(root, 1000000, -1000000)
# upperB = max(upperB, node.val)
# lowerB = min(lowerB, node.val)
#
# dfs(node.left, upperB, min(lowerB, node.val))
# dfs(node,right, max(upperB, node.val), lowerB)
