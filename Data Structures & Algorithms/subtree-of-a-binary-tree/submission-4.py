# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def sameTree(self, s: [TreeNode], t: [TreeNode]) -> bool:
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        # at least one of the trees is empty
        return False
        


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
