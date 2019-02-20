class Solution:
    def generateParenthesis(self, n):
        return self.help([], n)

    def isValidParen(self, parens, n):
        if len(parens) > 2*n:
            return False
        acc = 0
        ob = 0
        for c in parens:
            ob += 1 if c == '(' else 0
            acc += 1 if c == '(' else -1
            if acc < 0 or ob > n:
                return False
        return True

    def help(self, acc, n):
        if self.isValidParen(acc, n) == False:
            return []
        if len(acc) == 2 * n:
            return [''.join(acc)]
        cp1 = acc[:]
        cp1.append('(')
        cp2 = acc[:]
        cp2.append(')')
        lst1 = self.help(cp1, n)
        lst2 = self.help(cp2, n)
        res = []
        res.extend(lst1)
        res.extend(lst2)
        # print (res)
        return res

s = Solution()
n = 3
print (s.generateParenthesis(n))
