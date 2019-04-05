class Solution:
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        longest = '' if n == 0 else s[0]
        dp = [[''] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = s[i]
        for d in range(1, n):
            for i in range(0, n):
                j = i + d
                if j >= n:
                    break
                if s[i] == s[j]:
                    if d == 2 or len(dp[i+1][j-1]) == j-i-1:
                        dp[i][j] = s[i] + dp[i+1][j-1] + s[j]
                        if len(dp[i][j]) > len(longest):
                            longest = dp[i][j]
        print (longest)
    """
    def longestPalindrome(self, s: str) -> str:
        def getMaxLenPalindrome(s, i, j):
            n = len(s)
            while i >= 0 and j < n and s[i] == s[j]:
                i, j = i-1, j+1
            return s[i+1:j]
        longest = ''
        n = len(s)
        if n < 2:
            return s
        for i in range(0, n):
            odd = getMaxLenPalindrome(s, i, i)
            even = getMaxLenPalindrome(s, i, i+1)
            if len(odd) > len(longest):
                longest = odd
            if len(even) > len(longest):
                longest = even
        print(longest)


sol = Solution()
# babab
s1 = 'bababacc'
# bbddbb
s2 = 'cbbddbbabc'
# ''
s3 = ''
# a
s4 = 'a'
# aaaaaaa
s5 = 'aaaaaaa'

sol.longestPalindrome(s1)
sol.longestPalindrome(s2)
sol.longestPalindrome(s3)
sol.longestPalindrome(s4)
sol.longestPalindrome(s5)

