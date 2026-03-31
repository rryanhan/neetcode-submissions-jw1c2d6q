# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, lower, upper):
            if not root:
                return True
            if lower < root.val < upper:
                return dfs(root.left, lower, min(root.val, upper)) and dfs(root.right, max(root.val, lower), upper)
            else:
                return False

        return dfs(root, -9999 , 9999)




# nodes to left have to be less than parents key
# nodes to the right have to be greater than parents key




        







        



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
