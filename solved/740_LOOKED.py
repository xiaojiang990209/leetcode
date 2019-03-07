class Solution:
    def deleteAndEarn(self, nums) -> int:
        dp = [0] * 10001
        for elem in nums:
            dp[elem] += elem
        for i in range(2, 10001):
            dp[i] = max(dp[i-1], dp[i-2] + dp[i])
        return dp[10000]

sol = Solution()
a1 = [3,4,2]
a2 = [2,2,3,3,3,4]
a3 = [2,2,3,3,3,4,4,4,5]
# 14, 16
print (sol.deleteAndEarn(a1))
print (sol.deleteAndEarn(a2))
print (sol.deleteAndEarn(a3))
