class Solution:
    def levelOrder(self, root):
        cur_level = []
        if root != None: cur_level.append(root)
        next_level = []
        res = []
        # while we still have deeper levels
        while len(cur_level) != 0:
            val = []
            next_level = []
            # pop all current level nodes and compute level order traversal
            while len(cur_level) != 0:
                node = cur_level.pop(0)
                val.append(node.val)
                if node.left != None: next_level.append(node.left)
                if node.right != None: next_level.append(node.right)
            res.append(val)
            # next_level becomes the next cur_level to traverse
            cur_level = next_level
        return res



