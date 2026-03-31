# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQueue = deque([p])
        qQueue = deque([q])

        while pQueue and qQueue:
            pNode = pQueue.popleft()
            qNode = qQueue.popleft()
            if not pNode and not qNode:
                continue
            if not pNode or not qNode or pNode.val != qNode.val:
                return False
            pQueue.append(pNode.left)
            pQueue.append(pNode.right)
            qQueue.append(qNode.left)
            qQueue.append(qNode.right)
        
        return True

       

        