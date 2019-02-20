# Possible other combinations:
# Impossible. HashMap contains all possible results of
# the numbers in C and D, and when we iterate over all
# numbers in A and B, we have essentially iterated over
# all possible combinations of A, B, C, D
class Solution:
    def fourSumCount(self, A, B, C, D):
        # Compute all sums in C, D:
        sum_map = {}
        for num1 in C:
            for num2 in D:
                if (num1 + num2) in sum_map:
                    sum_map[num1+num2] += 1
                else:
                    sum_map[num1+num2] = 1

        count = 0
        for num1 in A:
            for num2 in B:
                if -(num1+num2) in sum_map:
                    count += sum_map[-(num1+num2)]
        return count

s = Solution()
A = [1,2]
B = [-2,-1]
C = [-1,2]
D = [0,2]
print (s.fourSumCount(A,B,C,D))

