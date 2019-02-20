class Solution:
    def minMoves2(self, nums):
        median = sorted(nums)[len(nums) // 2]
        return sum(list(map(lambda x: abs(median-x), nums)))
s = Solution()

lst = [1,2,3]
print (s.minMoves2(lst))
