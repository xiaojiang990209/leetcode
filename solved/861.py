class Solution:
    def matrixScore(self, A):
        for i, row in enumerate(A):
            if row[0] == 0:
                row[:] = [0 if elem == 1 else 1 for elem in row]
        transpose = [[row[i] for row in A] for i in range(len(A[0]))]
        print (A)
        for i, row in enumerate(transpose):
            if row.count(1) < row.count(0):
                row[:] = [0 if elem == 1 else 1 for elem in row]
        A = [[row[i] for row in transpose] for i in range(len(transpose[0]))]
        print (A)
        return sum([int(''.join(map(str, lst)), 2) for lst in A])


sol = Solution()
A = [[0,0,1,1], [1,0,1,0], [1,1,0,0]]
print (sol.matrixScore(A))
