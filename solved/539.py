class Solution:
    def findMinDifference(self, timePoints):
        lst = []
        for s in timePoints:
            tp = s.split(":")
            lst.append(int(tp[0]) * 60 + int(tp[1]))
        # Use bucket sort?
        sorted_lst = [0 for i in range(24*60)]
        for tp in lst:
            sorted_lst[tp] += 1
        first, last, prevTp, min_diff = -1, -1, -1, 24*60+1
        for tp in range(len(sorted_lst)):
            if sorted_lst[tp] == 1:
                first = tp if first == -1 else first
                if prevTp == -1:
                    prevTp = tp
                else:
                    min_diff = min(min_diff, tp - prevTp)
                    prevTp = tp
            elif sorted_lst[tp] != 0:
                return 0
        last = prevTp
        min_diff = min(min_diff, 24*60-last+first)
        return min_diff

s = Solution()
tp = ["00:00", "23:59", "00:00"]
print (s.findMinDifference(tp))
