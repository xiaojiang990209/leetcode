class Solution:
    def nextGreaterElements(self, nums):
        next_great = []
        for i in range(len(nums)):
            start = i
            next = start + 1
            cur_max = nums[start]
            while True:
                if next == len(nums): next = 0
                if next == start: break
                cur_max = max(cur_max, nums[next])
                if cur_max > nums[start]:
                    break
                if next < start:
                    if nums[next] == nums[start]:
                        cur_max = next_great[next]
                        break
                    if nums[start] > nums[next] and next_great[next] > nums[start]:
                        cur_max = next_great[next]
                        break
                next += 1
            next_great.append(-1 if cur_max == nums[start] else cur_max)
        return next_great

s = Solution()
nums = [1,2,3,4,3]
nums2 = [1,3,2,1]
print (s.nextGreaterElements(nums2))
