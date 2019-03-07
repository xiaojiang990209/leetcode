# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        level = [root]
        seenNone = False
        while len(level) != 0:
            node = level.pop(0)
            if node == None:
                seenNone = True
                continue
            if seenNone and node != None:
                return False
            level.append(node.left)
            level.append(node.right)
        return True
