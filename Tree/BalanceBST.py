# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        def helper(node):
            if not node:
                return []
            arr = helper(node.left) +[node] + helper(node.right)
            return arr
        inorder = (helper(root))
        root = TreeNode(inorder[len(inorder)//2])
        def builder2(inorder):
            if not inorder:
                return
            root = inorder[len(inorder)//2]
            root.left = builder2(inorder[:len(inorder)//2])
            root.right = builder2(inorder[len(inorder)//2+1:])
            return root
        return builder2(inorder)
