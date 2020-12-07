class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        
        result = []
        stack = []
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left if root.left else root.right
            
            root = stack.pop()  #Last in First Out
            result.append(root.val)
            
            if stack and stack[-1].left == root:
                root = stack[-1].right
            else:
                root = None
        return result
        
        
