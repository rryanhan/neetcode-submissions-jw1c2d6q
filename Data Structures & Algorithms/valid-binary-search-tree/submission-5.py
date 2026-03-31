# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        q = deque([(root, -9999, 9999)])
        while q:
            node, lower, upper = q.popleft()
            if lower < node.val < upper:
                if node.left:
                    q.append((node.left, lower, node.val))
                if node.right:
                    q.append((node.right, node.val, upper))
            else:
                return False
        return True




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
