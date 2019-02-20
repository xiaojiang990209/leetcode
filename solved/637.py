class Solution:
    def averageOfLevels(self, root):
        level_averages = []
        cur_level = []
        cur_level.append(root)
        while True:
            level_sum = 0
            next_level = []
            level_len = len(cur_level)
            while len(cur_level) != 0:
                node = cur_level.pop(0)
                level_sum += node.val
                if node.left != None:
                    next_level.append(node.left)
                if node.right != None:
                    next_level.append(node.right)
            level_averages.append(level_sum / level_len)
            if len(next_level) == 0:
                break
            cur_level = next_level
        return level_averages
