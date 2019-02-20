class Solution:
    def largestValues(self, root):
        res = []
        cur_level = []
        if root == None:
            return res
        cur_level.append(root)
        while len(cur_level) != 0:
            next_level = []
            cur_level_max = cur_level[0].val
            for node in cur_level:
                cur_level_max = cur_level_max if cur_level_max >= node.val else node.val
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
            cur_level = next_level
            res.append(cur_level_max)
        return res

