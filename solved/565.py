class Solution:
    def arrayNesting(self, nums):
        max_len = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                continue
            cur_len = 0
            j = i
            while nums[j] >= 0:
                cur_len += 1
                next_index = nums[j]
                nums[j] = -1
                j = next_index
            max_len = max(max_len, cur_len)
        return max_len

s = Solution()
A = [5,4,0,3,1,6,2]
print (s.arrayNesting(A))

















