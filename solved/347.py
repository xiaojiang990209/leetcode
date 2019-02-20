class Solution:
    def topKFrequent(self, nums, k):
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # to keep track of frequency. Since we have nums items,
        # we at most have an array of size nums
        bucket = [[] for i in range(len(nums) + 1)]
        for e in freq.items():
            bucket[e[1]].append(e[0])
        res = []
        for i in range(len(nums), -1, -1):
            for e in bucket[i]:
                res.append(e)
        return res[0:k]

s = Solution()
nums = [1]
k = 1
print (s.topKFrequent(nums, k))


