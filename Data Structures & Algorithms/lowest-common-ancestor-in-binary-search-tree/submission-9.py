# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if p.val <= root.val <= q.val or p.val >= root.val >= q.val:
            return root
        if root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)


# if the root is in between p and q, return it
# if the node is greater than q, move to the left
# if the node is less than p, move to the right
#
#
#               2
#
#.       null         3
#
# q=2, p=3
#
#