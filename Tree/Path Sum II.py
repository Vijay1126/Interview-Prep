# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        output = []
        def helper(node, curr, path):
            nonlocal output
            if node:
                curr+= node.val
                path.append(node.val)
                helper(node.left,curr,path.copy())
                helper(node.right, curr, path[:])
                if not node.left and not node.right:
                    if curr == sum:
                        output.append(path)
                return output
        return helper(root, 0, [])
