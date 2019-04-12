# Fucking stupid generalization
# K sum => K-1 sum => .... => 2sum
# O(n^(K-1))
class Solution:
    def fourSum(self, nums, target):
        def inclo(lo, a):
            while lo < len(a) and a[lo] == a[lo-1]:
                lo += 1
            return lo
        def dechi(hi, a):
            while hi >= 0 and a[hi] == a[hi+1]:
                hi -= 1
            return hi

        a = sorted(nums)
        n = len(a)
        res = []
        d = {}
        for i in range(n):
            if i > 0 and a[i-1] == a[i]:
                continue
            for j in range(i+1, n):
                if j > i+1 and a[j-1] == a[j]:
                    continue
                t = target - a[i] - a[j]
                lo, hi = j+1, n-1
                while lo < hi:
                    if a[lo] + a[hi] < t:
                        lo += 1
                        lo = inclo(lo, a)
                    elif a[lo] + a[hi] > t:
                        hi -= 1
                        hi = dechi(hi, a)
                    else:
                        res.append([a[i], a[j], a[lo], a[hi]])
                        lo, hi = lo+1, hi-1
                        lo = inclo(lo, a)
                        hi = dechi(hi, a)
        return res


nums = [-1,0,-5,-2,-2,-4,0,1,-2]
target = -9
# -5, -4, -2,-2,-2,-1,0,0,1
sol = Solution()
print (sol.fourSum(nums, target))
