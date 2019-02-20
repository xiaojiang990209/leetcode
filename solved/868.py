import sys

class Solution:
    def binaryGap(self, N):
        binary = list(map(int,bin(int(N))[2:]))
        one_count = binary.count(1)
        if one_count == 0 or one_count == 1:
            return 0
        cur_len = 0
        max_len = 1
        for bit in binary:
            if bit == 1:
                max_len = max(cur_len, max_len)
                cur_len = 1
            else:
                cur_len = cur_len + 1
        return max_len


print (Solution().binaryGap(sys.argv[1]))
