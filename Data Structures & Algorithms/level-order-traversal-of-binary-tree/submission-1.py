# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        q = collections.deque()
        q.append(root)

        while q: # while the queue exists
            length = len(q) #get the length of the queue
            listToAdd = []
            for i in range(length): # pop every current value in the queue
                node = q.popleft()
                if node:
                    listToAdd.append(node.val) #add the node to the list to add
                    q.append(node.left) # add children into the queue
                    q.append(node.right)
            if listToAdd: # you need to make sure the list actually contains stuff in it before adding to result
                result.append(listToAdd)

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
        