# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = self.calculateDepth(root)
        if depth == 0:
            return 1
        #The last row can essentially have values ranging from 1 to 2**d-1
        left = 1
        right = 2**depth-1
        
        while left<=right:
            #this is for binary searching the node that exists
            mid = (left+right)//2
            if self.exists(mid, root, depth):
                left = mid+1
            else:
                right = mid-1
            
        return (2**depth-1)+left
    
    def exists(self, index, node, d):
        
        left = 0
        right = 2**d-1
        
        for _ in range((d)):
            mid = (left+right)//2
            if index>mid:
                node = node.right
                left = mid + 1
            else:
                node = node.left
                right = mid 
            
        return node is not None
                
                
            
    def calculateDepth(self, node):
        d = 0
        while node.left:
            d+=1
            node = node.left
        return d
            
        
