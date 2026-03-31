# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pQ = deque([p])
        qQ = deque([q])

        while pQ and qQ:
            for _ in range(len(pQ)):
                pNode = pQ.popleft()
                qNode = qQ.popleft()
                if not pNode and not qNode:
                    continue
                if (not qNode and pNode) or (qNode and not pNode) or (pNode.val != qNode.val):
                    return False
                pQ.append(pNode.left)
                pQ.append(pNode.right)
                qQ.append(qNode.left)
                qQ.append(qNode.right)
        return True


       

        