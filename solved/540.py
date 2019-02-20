class Solution:
    def singleNonDuplicate(self, nums):
        # find mid
        mid = len(nums) // 2
        if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
            return nums[mid]
        if nums[mid] == nums[mid-1] and mid % 2 == 0:
            self.singleNonDuplicate(nums[0: mid-2])

