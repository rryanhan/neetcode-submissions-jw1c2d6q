# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node, depth):
            if not node:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            if node.left:
                dfs(node.left, depth + 1)
            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 0)

        return res
        


        
        

        
                
        
    
        

#                   append node
#              append [node.left, node.right]
#       append[node.left, node.right, node.left, node.right]
#
#
#
#
#
#
#
#
#
#
#
        