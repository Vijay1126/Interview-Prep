class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        return self.helper(root)
    def helper(self, node):
        if node:
            if node.left:
                node.left.next = node.right
            if node.next:
                if node.right:
                    node.right.next = node.next.left
            self.helper(node.left)
            self.helper(node.right)
            return node
