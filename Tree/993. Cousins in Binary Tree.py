# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        stack = deque([root])
        
        while stack:
            xFound = False
            yFound = False
            for i in range(len(stack)):
                node = stack.popleft()
                if node.val == x:
                    xFound = True
                elif node.val == y:
                    yFound = True
                if node.left and node.right:
                    if (node.left.val == x and node.right.val == y) or (node.right.val== x and node.left.val == y):
                        return False
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
                    
                if xFound and yFound:
                    return True
        return False
                
