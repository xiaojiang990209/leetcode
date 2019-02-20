class Solution:
    def findBottomLeftValue(self, root)
        return self.findBottomleftValueHeight(root)[0]

    def findBottomLeftValueHeight(self, root):
        if root == None:
            return (None, None)
        if root.left == None and root.right == None:
            return (root.val, 0)
        (left_val, left_height) = self.findBottomLeftValueHeight(root.left)
        (right_val, right_height) = self.findBottomLeftValueHeight(root.right)
        if left_height == None:
            return (right_val, right_height + 1)
        elif right_height == None:
            return (left_val, left_height + 1)
        elif left_height < right_height:
            return (right_val, right_height + 1)
        else:
            return (left_val, left_height + 1)
