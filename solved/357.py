# For this quesgtion, we utlize dp with a little bit of combinatorics.

# let f(k) = # of numbers with unique digits with length k
# For instance,
# f(1) = 10 = {0,1,2,3,4,5,6..9}
# f(2) = 91 = {10, 12, 13...98}
# In general, we find out that for a number with length k 1XXXXXX:
# the number of unique numbers we could have is:
# 9C1 {1..9} * 9C1 {0..9 exclude previous one} * 8C1 * 7C1 * ... * (9-k+2)C1
# = 9 * 9 * 8 * 7 * (9-k+2)
# Having this, all we have to do in the end is just to sum the numbers

class Solution:
    def countNumbersWithUniqueDigits(self, n):
        def find_unique(k):
            if k == 0:
                return 1
            else:
                end = 11 - k
                num = 9
                for i in range(9, end - 1, -1):
                    num *= i
                return num
        num = 0
        for k in range(0, n+1):
            num += find_unique(k)
        return num


s = Solution()
n = 1
n2 = 2
print (s.countNumbersWithUniqueDigits(n))
print (s.countNumbersWithUniqueDigits(n2))


