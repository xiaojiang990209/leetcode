# For this question, we define binary search to be a little different
# than what we were used to do:
# The notion of search space, in this question, is not the array itself,
# but the range of possible numbers, namely 1..n.
# By binary searching the range 1..n, and counting the # of numbers that
# are less than the mid, and comparing that with the expected value,
# we can arrive at the solution in O(nlgn) time

class Solution:
    def findDuplicate(self, nums):
        lo, hi = 1, len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            count = 0
            for e in nums:
                if e <= mid: count += 1
            if count <= mid: lo = mid + 1
            else: hi = mid
        return lo

s = Solution()
lst = [1,3,4,2,2]
lst2 = [3,1,3,4,2]
print (s.findDuplicate(lst))
print (s.findDuplicate(lst2))
