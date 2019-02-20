class Solution:
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
            print (bin(i))
        i = i - 1
        return i^num

sol = Solution()
print (sol.findComplement(1))
