import bisect
class Solution:
    def isSubsequence(self, s, t):
        alphabet = {}
        for i, letter in enumerate(t):
            if letter not in alphabet: alphabet[letter] = []
            alphabet[letter].append(i)
        prev = 0
        for letter in s:
            if letter not in alphabet: return False
            j = bisect.bisect_left(alphabet[letter], prev)
            if j == len(alphabet[letter]): return False
            prev = alphabet[letter][j] + 1
        return True

sol = Solution()
s1 = "abc"
t1 = "ahbgdc"
s2 = "axc"
t2 = "ahbgdc"
print (sol.isSubsequence(s1, t1))
print (sol.isSubsequence(s2, t2))

