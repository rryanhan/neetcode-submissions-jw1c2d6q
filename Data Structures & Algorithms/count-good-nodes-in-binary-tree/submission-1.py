# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        currentNode = -101
        count = 0
        def dfs(node, maxVal):
            nonlocal count
            if node is None:
                return 0
            if node.val >= maxVal:
                count = count + 1
            dfs(node.left, max(maxVal, node.val))
            dfs(node.right, max(maxVal, node.val))

        dfs(root, currentNode)
        return count

#             if current node is greater than the max value we see, count += 1
#.        find the maxvalue on the path
#           if maxVal is null: += 1 count, and set to current Node
#
#
#
#
#
        
        