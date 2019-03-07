class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cur = [1 for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                # cur[j] = prev[j] + cur[j-1]
                # Since prev = cur, we can have cur[j] = cur[j] + cur[j-1], so that we eliminate prev
                cur[j] += cur[j-1]
        return cur[n-1]

m1, n1 = 3, 2
m2, n2 = 7, 3
sol = Solution()
print (sol.uniquePaths(m1, n1))
print (sol.uniquePaths(m2, n2))
