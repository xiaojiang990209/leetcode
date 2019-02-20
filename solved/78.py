class Solution:
    def subsets(self, nums):
        def subset_help(res, acc, lst):
            res.append(acc[:])
            for i in range(len(lst)):
                temp = acc[:]
                temp.append(lst[0])
                lst.pop(0)
                lst2 = lst[:]
                subset_help(res, temp, lst2)
        res = []
        subset_help(res, [], nums)
        return res

s = Solution()
nums = [1,2,3]
print (s.subsets(nums))
