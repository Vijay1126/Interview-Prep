# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False
        if self.isSame(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSame(self, a, b):
        if not a and not b:
            return True
        if not a or not b:
            return False
        if a.val!=b.val:
            return False
        return self.isSame(a.left, b.left) and self.isSame(a.right, b.right)
        
