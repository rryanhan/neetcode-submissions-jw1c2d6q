# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def dfs(node, level):
            if not node:
                return None
            if len(result) == level:
                result.append(node.val)
            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        
        dfs(root, 0)
        return result

#.             1
#.       2           3
#.    4     5      6    7
# result = []
# if the depth is equal to result, append it to result. move to right
#
# [1, 3, 7]
#
#
#

            


        