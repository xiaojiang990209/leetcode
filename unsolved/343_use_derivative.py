class Solution:
    def integerBreak(self, n):
        max_ar = []
        max_ar.append(0)
        max_ar.append(1)
        for i in range(2, n+1):
            cur_max = 0
            for j in range(1, i // 2 + 1):
                cur_max = max(cur_max, max(j*(i-j), j*max_ar[i-j]))
            max_ar.append(cur_max)
        print (max_ar)
        return max_ar[-1]

s = Solution()
n1 = 2
n2 = 10
print (s.integerBreak(n1))
print (s.integerBreak(n2))

