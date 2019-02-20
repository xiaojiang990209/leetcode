class Solution:
    def flatten(self, root):
        def flat_help(root):
            if root == None: return None
            tail_l = flat_help(root.left)
            tail_r = flat_help(root.right)
            if tail_l not None:
                tail_l.right = root.right
                root.right = root.left
            root.left = None
            if tail_r not None: return tail_r
            elif tail_l not None: return tail_l
            else: return root
        flat_help(root)

