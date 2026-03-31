# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left = self.findHeight(root.left)
        right = self.findHeight(root.right)

        if left-right > 1 or right-left > 1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        
    
    def findHeight(self, curr: Optional[TreeNode]) -> int:
        if not curr:
            return 0
        left = self.findHeight(curr.left)
        right = self.findHeight(curr.right)
        return 1 + max(left, right)





# get the max height of left and right at every node, and see if it differs > 1
# 
#
#
#
#
#
        