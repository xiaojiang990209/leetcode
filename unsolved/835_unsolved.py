class Solution:
    def largestOverlap(self, A, B):
        N = len(A)
        setA = set()
        setB = set()
        first_pos = (-1, -1)
        largeA = False
        for i in range(N):
            for j in range(N):
                if A[i][j] == 1:
                    if first_pos == (-1, -1):
                        largeA = True
                        first_pos = (i, j)
                    setA.add((i, j))
                if B[i][j] == 1:
                    if first_pos == (-1, -1):
                        largeA = False
                        first_pos = (i, j)
                    setB.add((i, j))
        res = 0
        tempA, tempB = set(setA), set(setB)
        for i in range(N):
            for j in range(N):
                count = 0
                for elem in tempA:
                    shift_elem = (i + elem[0], j + elem[1])
                    if shift_elem in setB: count += 1
                res = max(res, count)
                count = 0
                for elem in tempB:
                    shift_elem = (i + elem[0], j + elem[1])
                    if shift_elem in setA: count += 1
                res = max(res, count)
        return res



sol = Solution()
A = [[1,1,0], [0,1,0], [0,1,0]]
B = [[0,0,0], [0,1,1], [0,0,1]]
print (sol.largestOverlap(A, B))


