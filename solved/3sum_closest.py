class Solution:
    def threeSumClosest(self, nums, target):
        a = sorted(nums)
        n = len(a)
        min_diff_sum = -1
        for i in range(n):
            j,k = i+1, n-1
            while j < k:
                s = a[i] + a[j] + a[k]
                d = abs(target - s)
                if d == 0:
                    return s
                if min_diff_sum == -1 or d < abs(min_diff_sum - target):
                    min_diff_sum = s
                if s > target:
                    k -= 1
                else:
                    j += 1
        return min_diff_sum

a = [-1,2,1,-4]
t = 1

print (Solution().threeSumClosest(a,t))



