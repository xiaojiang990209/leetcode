class Solution:
    def threeSum(self, nums):
        # First attempt: cache value -> index into dict
        res = []
        n = len(nums)
        a = sorted(nums)
        for i in range(n):
            if i > 0 and a[i-1] == a[i]:
                continue
            goal = -a[i]
            j,k = i + 1, n - 1
            while j < k:
                if a[j] + a[k] > goal:
                    k -= 1
                elif a[j] + a[k] < goal:
                    j += 1
                else:
                    res.append([a[i], a[j], a[k]])
                    j += 1
                    k -= 1
                    while j < n and a[j-1] == a[j]:
                        j += 1
                    while k >= 0 and a[k+1] == a[k]:
                        k -= 1
        return res

a = [-1,0,1,2,-1,-4]
b = [0,0,0]
sol = Solution()
print (sol.threeSum(a))
print (sol.threeSum(b))
