class Solution:
    def reconstructQueue(self, people):
        # Sort people first
        people.sort(key=lambda x: (-x[0], x[1]))
        N = len(people)
        res = []
        for pair in people:
            res.insert(pair[1], pair)
        return res

s = Solution()
lst = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

print (s.reconstructQueue(lst))
