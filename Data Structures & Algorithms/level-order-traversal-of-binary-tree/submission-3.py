# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        queue = deque([root])
        

        while queue:
            levelArray = []
            for i in range(len(queue)):
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                levelArray.append(node.val)
            result.append(levelArray)
        return result
                
        
    
        

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
        