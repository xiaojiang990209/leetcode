class Solution:
    def addOneRow(self, root, v, d):
        def help(root, v, d, acc, isLeft):
            if acc == d:
                n = TreeNode(v)
                if isLeft: n.left = root
                else: n.right = root
                return n
            if root == None: return None
            root.left = help(root.left, v, d, acc + 1, True)
            root.right = help(root.right, v, d, acc + 1, False)
            return root
        return help(root, v, d, 1, True)
