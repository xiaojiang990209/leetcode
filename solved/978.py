class Solution:
    def maxTurbulenceSize(self, A):
        max_so_far = 1
        # max_end_here[0] = len of longest turb subarray with A[i] > A[i+1]
        # max_end_here[1] = len of longest turb subarray with A[i] < A[i+1]
        max_end_here = [1,1]
        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                max_end_here[0] = 1 + max_end_here[1]
                max_end_here[1] = 1
            elif A[i] < A[i+1]:
                max_end_here[1] = 1 + max_end_here[0]
                max_end_here[0] = 1
            else:
                max_end_here = [1,1]
            max_so_far = max(max_so_far, max_end_here[0], max_end_here[1])
        return max_so_far


sol = Solution()
A1 = [9,4,2,10,7,8,8,1,9]
A2 = [4,8,12,16]
A3 = [100]
print (sol.maxTurbulenceSize(A1))
print (sol.maxTurbulenceSize(A2))
print (sol.maxTurbulenceSize(A3))

