class Solution:
    def lenLongestFibSubseq(self, A):
        n = len(A)
        dp = [[0] * n for i in range(n)]
        elems = {}
        global_max = 0
        for index, elem in enumerate(A):
            elems[elem] = index
        for i in range(0, n):
            for j in range(1, i):
                if A[i]-A[j] in elems:
                    k = elems[A[i]-A[j]]
                    if k < j:
                        dp[i][j] = max(dp[j][k] + 1, 3)
                        global_max = max(global_max, dp[i][j])
        # print (dp)
        return global_max

A = [2,4,7,8,9,10,14,15,18,23,32,50]
B = [1,2,3,4,5,6,7,8]
C = [1,3,7,11,12,14,18]
D = [2,5,6,7,8,10,12,17,24,41,65]

# 3: {2:3}
# 4: {3:3}
# 5: {3:4}

sol = Solution()
print (sol.lenLongestFibSubseq(A))
print (sol.lenLongestFibSubseq(B))
print (sol.lenLongestFibSubseq(C))
print (sol.lenLongestFibSubseq(D))


