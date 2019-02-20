class Solution:
    def reverseString(self, s):
        # length = len(s)
        # sList = list(s)
        # for i in range(length // 2):
            # temp = sList[i]
            # sList[i] = sList[length - 1 - i]
            # sList[length - 1 - i] = temp
        # return ''.join(sList)
# Better solution using divide and conquer
    def reverseString(self, s):
        length = len(s)
        if length < 2:
            return s
        mid = length // 2
        return reverseString(s[mid:]) + reverseString(s[0:mid])
