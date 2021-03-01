# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        stack = deque([root])
        output = []
        while stack:
            curr = stack.popleft()
            if curr:
                output.append(curr.val)
            else:
                output.append(None)
            if curr!=None:
                stack.append(curr.left)
                stack.append(curr.right)
        print(output)
        return output
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        print(data)
        i = 1
        root = TreeNode(data[0])
        queue = deque([root])
        while queue and i<len(data):
            curr = queue.popleft()
            
            if data[i]!=None:
                
                node = TreeNode(data[i])
                curr.left = node
                queue.append(node)
            i+=1
            if data[i]!=None:
                node = TreeNode(data[i])
                curr.right = node
                queue.append(node)
            i+=1
        
        return root
            
            
            
        
        
        
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
