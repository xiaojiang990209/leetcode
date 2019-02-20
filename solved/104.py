class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        return 1 + max(maxDepth(root.left), maxDepth(root.right))
