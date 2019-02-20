class Solution:
    def minDistance(self, word1, word2):
        ##def helper(s1, s2, acc):
        ##    if s1 == s2: return acc
        ##    if len(s1) > 0 and len(s2) > 0 and s1[0] == s2[0]:
        ##        return helper(s1[1:], s2[1:], acc)
        ##    acc1 = acc2 = acc
        ##    validLeft = validRight = False
        ##    if len(s1) > 0:
        ##        acc1 = helper(s1[1:], s2, 1 + acc1)
        ##        validLeft = True
        ##    if len(s2) > 0:
        ##        acc2 = helper(s1, s2[1:], 1 + acc2)
        ##        validRight = True
        ##    if validLeft and validRight: return min(acc1, acc2)
        ##    elif validLeft: return acc1
        ##    else: return acc2
        ##return helper(word1, word2, 0)
        len1 = len(word1) + 1
        len2 = len(word2) + 1
        table = [[0 for j in range(len2)] for i in range(len1)]
        for i in range(len1): table[i][0] = i
        for j in range(len2): table[0][j] = j
        for i in range(1, len1):
            for j in range(1, len2):
                if word1[i-1] == word2[j-1]:
                    table[i][j] = table[i-1][j-1]
                else:
                    table[i][j] = min(1 + table[i-1][j], 1 + table[i][j-1])
        return table[len1 - 1][len2 - 1]


sol = Solution()
s1 = "sea"
s2 = "eat"
print (sol.minDistance(s1, s2))
