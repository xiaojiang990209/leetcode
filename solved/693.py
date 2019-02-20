import sys

class Solution:
    def hasAlternatingBits(self, n):
        mask = 1
        prev_bit = -1
        while n != 0:
            bit = n & mask
            if bit == prev_bit:
                return False
            prev_bit = bit
            n = n >> 1
        return True

print (Solution().hasAlternatingBits(int(sys.argv[1])))
