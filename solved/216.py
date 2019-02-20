class Solution:
    def combinationSum(self, k, n):
        def combinSumHelp(k, n, acc, res):
            length = len(res)
            if length > k or acc > n: return []
            if length == k and acc == n: return [res]
            start = 1 if length == 0 else res[length-1] + 1
            result = []
            for i in range(start, 10):
                cp = res[:]
                cp.append(i)
                result.extend(combinSumHelp(k, n, acc + i, cp))
            return result
        return combinSumHelp(k, n, 0, [])

s = Solution()
k1, n1 = 3, 7
k2, n2 = 3, 9
print (s.combinationSum(k1, n1))
print (s.combinationSum(k2, n2))


