class Solution:
    def generateMatrix(self, n: int):
        m = [[0] * n for _ in range(n)]
        i,j,di,dj = 0,0,0,1
        num = 0
        while num != n*n:
            num += 1
            m[i][j] = num
            if m[(i+di)%n][(j+dj)%n] != 0:
                di, dj = dj, -di
            i += di
            j += dj
        return m

sol = Solution()
n1 = 3
n2 = 4
n3 = 1
n4 = 2
print (sol.generateMatrix(n1))
print (sol.generateMatrix(n2))
print (sol.generateMatrix(n3))
print (sol.generateMatrix(n4))
