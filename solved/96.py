class Solution:
    def numTrees(self, n: 'int') -> 'int':
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, i//2 + 1):
                l,r = j-1,i-j
                dp[i] += dp[l]*dp[r]
            dp[i] *= 2
            if i % 2 == 1:
                dp[i] += dp[i//2]*dp[i//2]
        return dp[n]

sol = Solution()
n1 = 3
n2 = 1
print (sol.numTrees(n1))
print (sol.numTrees(n2))

