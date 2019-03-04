class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for i in range(n)]
        for i in range(n):
            dp[i][i] = 1
        for i in range(1, n):
            for j in range(i-1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i-1][j+1]+2
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i-1][j])
        return dp[n-1][0]

sol = Solution()
str1 = "bbbab"
str2 = "cbbd"
str3 = "abcdefghijklmn"
# str4 = "abcdefbghibjklbolbb"
str4 = "abcbebb"
print (sol.longestPalindromeSubseq(str1))
print (sol.longestPalindromeSubseq(str2))
print (sol.longestPalindromeSubseq(str3))
print (sol.longestPalindromeSubseq(str4))
