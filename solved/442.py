class Solution:
    def findDuplicates(self, nums):
        # Given problem specification, 1 <= nums[i] <= n
        # Thus, we use array indices to memorize the indices
        # visited.
        res = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x) - 1] *= -1
        return res


s = Solution()
args = [4,3,2,7,8,2,3,1]
print (s.findDuplicates(args))
