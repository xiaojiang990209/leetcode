import random
class Solution:
    def kthSmallest(self, root, k):
        def help(root, k):
            if root == None:
                return (None, 0)
            size = 0
            left = help(root.left, k)
            if left[0] != None: return left
            size += (left[1] +1)
            if k == size: return (root.val, k)
            right = help(root.right, k - size)
            if right[0] != None: return right
            size += right[1]
            return (None, size)
        return help(root, k)[0]

