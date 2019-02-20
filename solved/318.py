class Solution:
    def maxProduct(self, words):
        values = []
        # Idea: Use integer's bit to represent existing character
        # i.e., 0011010 => {'b','d','e'}
        max_len = 0
        for word in words:
            val = 0
            for letter in word:
                val |= 1 << (ord(letter) - ord('a'))
            values.append(val)
        for i in range(len(values)):
            for j in range(i+1, len(values)):
                # If words[i], words[j] do not share common character,
                # then their bit representation 'and' is 0, since at
                # no position is values[i] and values[j] sharing a both
                # toggled bit
                if (values[i] & values[j] == 0):
                    max_len = max(max_len, len(words[i]) * len(words[j]))
        return max_len




        # this is the original version using set
        # words_lst = list(map(lambda e: (set(list(e)), len(e)), words))
        # length = len(words_lst)
        # max_len = 0
        # for i in range(length):
            # for j in range(i+1, length):
                # if words_lst[i][0].isdisjoint(words_lst[j][0]):
                    # max_len = max(max_len, words_lst[i][1] * words_lst[j][1])
        # return max_len


s = Solution()
t1 = ["abcw", "baz","foo","bar","xtfn","abcdef"]
t2 = ["a","ab","abc","d","cd","bcd","abcd"]
t3 = ["a","aa","aaa","aaaa"]

print (s.maxProduct(t1))
print (s.maxProduct(t2))
print (s.maxProduct(t3))

