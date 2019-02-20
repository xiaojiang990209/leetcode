class Solution:
    def maxChunksToSorted(self, arr):
        def help(arr, start, end):
            for i in range(start, end+1):
                if arr[i] > end or arr[i] < start:
                    return False
            return True
        length = len(arr)
        start = 0
        count = 0
        while start < length:
            for i in range(start, length):
                if help(arr, start, i):
                    start = i + 1
                    count += 1
        return count
    def maxChunksToSortedImproved(self, arr):
        max_ar = []
        count = 0
        for i in range(len(arr)):
            if i == 0: max_ar[0] = arr[0]
            else: max_ar[i] = max(max_ar[i-1], arr[i])
        for i in range(len(max_ar)):
            if max_ar[i] == i:
                count += 1
        return count

s = Solution()
t1 = [4,3,2,1,0]
t2 = [1,0,2,3,4]
t3 = [1,2,0,3]
print (s.maxChunksToSorted(t1))
print (s.maxChunksToSorted(t2))
print (s.maxChunksToSorted(t3))
