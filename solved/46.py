class Solution:
    def permute(self, nums):
        return self.permute_help([], nums)

    def permute_help(self, permute, rest):
        if len(rest) == 0:
            return [permute]
        permute_list = []
        for i in range(len(rest)):
            num = rest[i]
            temp = permute[:]
            temp_rest = rest[:]
            temp_rest.pop(i)
            temp.append(num)
            permute_list.extend(self.permute_help(temp, temp_rest))
        return permute_list

s = Solution()
nums = [1,2,3]
print (s.permute(nums))
