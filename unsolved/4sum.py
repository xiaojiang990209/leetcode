class Solution:
    def fourSum(self, nums, target):
        a = sorted(nums)
        n = len(a)
        for i in range(n):
            for j in range(i+1, n):

