class Solution:
    def findLongestWord(self, s, d) -> str:
        def can_form(s, d):
            if len(s) < len(d):
                return False
            index = 0
            for c in s:
                if d[index] == c:
                    index += 1
                if index == len(d):
                    break
            return index == len(d)
        max_len = 0
        max_elem = ""
        for elem in d:
            if can_form(s, elem) and (len(elem) > max_len or (len(elem) == max_len and elem < max_elem)):
                max_len = len(elem)
                max_elem = elem
        return max_elem

sol = Solution()
s = "abpcplea"
s2 = "asadljapasjddsapidsalsaklaslhdaemosdlsakjdnkadslkjsaey"
d1 = ["ale", "apple", "monkey", "plea"]
d2 = ["a","b","c"]

print (sol.findLongestWord(s, d1))
print (sol.findLongestWord(s2, d1))
print (sol.findLongestWord(s, d2))

