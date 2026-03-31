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
            # if children are inbalanced, return false
            # see if height difference are no greater than 1
            # recurse
            isBalanced = left[0] and right[0]
            correctHeight = abs(left[1] - right[1]) <= 1
            return [isBalanced and correctHeight, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]

        

# check height of current node, and if its children are also balanced