class Solution:
    def findDiagonalOrder(self, matrix):
        def next_state(i, j, M, N):
            if (i == 0 and j < N - 1) or i == M - 1:
                return (i, j+1)
            if (j == 0 and i < M - 1) or j == N - 1:
                return (i+1, j)
        if len(matrix) == 0:
            return []
        M, N = len(matrix), len(matrix[0])
        i,j,di,dj = 0,0,-1,1
        res = []
        for k in range(M+N-1):
            while i >= 0 and i < M and j >= 0 and j < N:
                res.append(matrix[i][j])
                i,j = i+di, j+dj
            i,j = next_state(i-di,j-dj,M,N)
            di, dj = -di, -dj
        return res

sol = Solution()
M = [
[1,2,3],
[4,5,6],
[7,8,9]
]

M2 = [
[1,2,3,4],
[5,6,7,8],
[9,10,11,12]
]

M3 = [
[1,2,3,4,5,6,7,8]
]

M4 = [
[1],
[2],
[3],
[4]
]

print (sol.findDiagonalOrder(M))
print (sol.findDiagonalOrder(M2))
print (sol.findDiagonalOrder(M3))
print (sol.findDiagonalOrder(M4))


