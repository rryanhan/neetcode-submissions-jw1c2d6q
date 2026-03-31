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
            left, right = dfs(root.left), dfs(root.right)
            balancedTree = left[0] and right[0] and abs(left[1]-right[1]) < 2
            return (balancedTree, 1+max(left[1], right[1]))
        
        return dfs(root)[0]
        
        

            
        

# get the max height of left and right at every node, and see if it differs > 1
# dfs
# if not root, return True 0
# left and right, call dfs on left and right
# heightD = absolute of left[1] - right[1] and left[0] and right[0]
# if heightD is true, return (heightD, and max height from left and right)
# 
# return dfs(root)[0]
        