import heapq
class Solution:
    def kthSmallest(self, matrix, k):
        lst = [e for sublist in matrix for e in sublist]
        heapq.heapify(lst)
        val = 0
        for i in range(k):
            val = heapq.heappop(lst)
        return val


s = Solution()
matrix = [
    [1,5,9],
    [10,11,13],
    [12,13,15]
]
k = 8
print (s.kthSmallest(matrix, k))
