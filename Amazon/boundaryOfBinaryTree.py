# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        
        leftBoundary = []
        if root.left or root.right:
            leftBoundary.append(root.val)
        left = root.left
        
        while left and (left.right or left.left):
            leftBoundary.append(left.val)
            if left.left:
                left = left.left
            elif left.right:
                left = left.right
    
        
        deq = deque([root])
        while deq:
            curr = deq.pop()
            
            if curr and not curr.left and not curr.right:
                leftBoundary.append(curr.val)
            if curr.right:
                deq.append(curr.right)
            if curr.left:
                deq.append(curr.left)
            
        
        
        right = root.right
        temp = []
        while right and (right.right or right.left):
            temp.append(right.val)
            if right.right:
                right = right.right
            else:
                right = right.left
            
        
        return(leftBoundary + temp[::-1])
