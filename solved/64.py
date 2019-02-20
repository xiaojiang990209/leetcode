class Solution:
    def minPathSum(self, grid: 'List[List[int]]') -> 'int':
        if grid is None:
            return 0
        m = len(grid)
        n = len(grid[0])
        memo = [[0] * n for i in range(m)]
        for i in range(m):
            memo[i][0] = (0 if i == 0 else memo[i-1][0]) + grid[i][0]
        for j in range(n):
            memo[0][j] = (0 if j == 0 else memo[0][j-1]) + grid[0][j]
        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = grid[i][j] + min(memo[i-1][j], memo[i][j-1])
        return memo[m-1][n-1]

matrix = [[1,3,1], [1,5,1], [4,2,1]]
sol = Solution()
print (sol.minPathSum(matrix))

