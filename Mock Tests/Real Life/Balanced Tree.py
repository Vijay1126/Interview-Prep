class Solution:
    def __init__(self):
        self.isValid = True
        
    def isBalanced(self, root: TreeNode) -> bool:
        height = self.helper(root, 0)
        return self.isValid
        
    def helper(self, node, height):
        if not node:
            return height
        lHeight = self.helper(node.left, height+1)
        rHeight = self.helper(node.right, height+1)
        
        if abs(lHeight-rHeight)>1:
            self.isValid = False
        return max(lHeight,rHeight)
        
