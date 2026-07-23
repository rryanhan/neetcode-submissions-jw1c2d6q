# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return 
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        return root

#           3
#       9       20
#             15   7
#   node.root = pre[0]
#   pre [3   9   20  15  7] 
#       -> node.left: [1: mid+1]
#       -> node.right: [mid + 1:]
#   in  [9   3   15  20  7] 
#       -> node.left: [:mid]
#       -> node.right: [mid+1:]
#
#
#
#
#