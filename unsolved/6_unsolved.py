class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = numRows
        res = []
        l = len(s)
        for i in range(n):
            m = 0
            k = i
            j = k + 2*(n - k - 1)
            while k < l:
                res.append(s[k])
                if k != 0 and k != n-1 and j < l:
                    res.append(s[j])
                if k == 0 or k == n-1:
                    k += 2*(n-k-1)
                else:
                    k += (n + 2)
                    j = k + 2*(n-k-1)
        print (''.join(res))

sol = Solution()

s = 'PAYPALISHIRING'

sol.convert(s, 3)
sol.convert(s, 4)



