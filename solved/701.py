class Solution:
    def insertIntoBST(self, root, val):
        if root.left == None and val < root.val:
            root.left = TreeNode(val)
        elif val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        elif root.right == None and val > root.val:
            root.right = TreeNode(val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        return root


































