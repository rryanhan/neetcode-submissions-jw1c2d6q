# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]
            left = dfs(root.left)
            right = dfs(root.right)
            if abs(left[1] - right[1]) > 1 or left[0] == False or right[0] == False:
                return [False, 1 + max(left[1], right[1])]
            else:
                return [True, 1 + max(left[1], right[1])]
            
        return dfs(root)[0]
        

# AT a given node,
# if abs(height of left - height of right) is greater than 1, false
# if any of left or right are false, false
# how do i get height?
# output of dfs = [boolean][height]
#
# 

            
        

# get the max height of left and right at every node, and see if it differs > 1
# dfs
# if not root, return True 0
# left and right, call dfs on left and right
# heightD = absolute of left[1] - right[1] and left[0] and right[0]
# if heightD is true, return (heightD, and max height from left and right)
# 
# return dfs(root)[0]
        