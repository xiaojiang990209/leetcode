class Solution:
    def splitListToParts(self, root, k):
        def move(res, root, count, step_size):
            for i in range(count):
                res.append(root)
                if root == None: continue
                for j in range(step_size - 1):
                    root = root.next
                prev = root
                root = root.next
                prev.next = None
            return root
        temp = root
        length = 0
        while temp != None:
            length += 1
            temp = temp.next
        slen = length // k
        large_count = length - k*slen
        small_count = k - large_count
        res = []
        small_start = move(res, root, large_count, slen + 1)
        move(res, small_start, small_count, slen)
        return res
