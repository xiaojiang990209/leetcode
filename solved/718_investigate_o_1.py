class Solution:
    """
    Apparently there is also an O(1) space complexity solution,
    investigate further
    """
    def findLength(self, A, B):
        prev = [0]*len(B)
        curr = [0]*len(B)
        global_max = 0
        for i in range(len(A)):
            curr=[0]*len(B)
            for j in range(len(B)):
                if A[i] == B[j]:
                    curr[j] = 1 if j-1<0 else prev[j-1]+1
            prev = curr
            global_max = max(global_max, max(curr))
        return global_max


A = [1,2,3,2,1]
B = [3,2,1,4,7,1,2,3,2,1]
A1 = [1,0,0,1,1]
A2 = [1,0,0,0,1]
sol = Solution()
print (sol.findLength(A,B))
print (sol.findLength(A1,A2))
