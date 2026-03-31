# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.identical(root, subRoot):
            return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def identical(self, p: [TreeNode], q: [TreeNode]) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (q and not p) or (p.val != q.val):
            return False
        return self.identical(p.left, q.left) and self.identical(p.right, q.right)


# conditions of a root being subroot
# all nodes have to match, and subroot.left and right has to be null
# helper fucntion to determine match function; called Function
# if not root then return False
# helper(left) and helper(right)
# return helper(left) or helper(right)
#
#
# helper function: takes in the root (p) and subroot (r)
# if not p and not q return true
# compare val, make sure they exist, see if equal
# if they are, call recursively on itself, left and right
#
#
