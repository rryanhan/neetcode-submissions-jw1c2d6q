# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, -101)])
        count = 0
        while queue:
            node, maxVal = queue.popleft()
            if node.val >= maxVal:
                count += 1
            if node.left:
                queue.append([node.left, max(node.val, maxVal)])
            if node.right:
                queue.append([node.right, max(node.val, maxVal)])
        return count     

        

#             if current node is greater than the max value we see, count += 1
#.        find the maxvalue on the path
#           if maxVal is null: += 1 count, and set to current Node
#
#
#
#
#
        
        