class Solution:
    def invertTree(self, root):
        if root == None: return None
        if root.left == None and root.right == None: return root
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)
        return root
