# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        def isCompleteTreeHelp(node):
            if node.left == None and node.right == None:
                return (0, True)
            if node.left == None:
                return (-1, False)
            l_h, l_c = isCompleteTreeHelp(node.left)
            if not l_c:
                return (-1, False)
            if node.right == None:
                return (l_h + 1, l_c if l_h == 0 else False)
            r_h, r_c = isCompleteTreeHelp(node.right)
            if abs(l_h-r_h) <= 1:
                return (min(l_h, r_h), l_c and r_c)
            else:
                return (-1, False)
        return isCompleteTreeHelp(root)[1]

