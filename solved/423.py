class Solution:
    def originalDigits(self, s):
        cache = [0 for i in range(10)]
        for letter in s:
            if letter == 'z': cache[0] += 1
            if letter == 'w': cache[2] += 1
            if letter == 'u': cache[4] += 1
            if letter == 'f': cache[5] += 1
            if letter == 'o': cache[1] += 1
            if letter == 'x': cache[6] += 1
            if letter == 'g': cache[8] += 1
            if letter == 'h': cache[3] += 1
            if letter == 'v': cache[7] += 1
            if letter == 'i': cache[9] += 1
        cache[1] -= (cache[0] + cache[2] + cache[4])
        cache[5] -= cache[4]
        cache[3] -= cache[8]
        cache[7] -= cache[5]
        cache[9] -= (cache[5] + cache[6] + cache[8])
        res = []
        for num, i in enumerate(cache):
            for j in range(i): res.append(str(num))
        return "".join(res)







sol = Solution()
s1 = "owoztneoer"
s2 = "fviefuro"
s3 = "twothreeonenineeightsixsevenfivefourthreetwoone"
s4 = "twothreeonenineeightsixsevenfivefourthreetwoone"
print (sol.originalDigits(s1))
print (sol.originalDigits(s2))
print (sol.originalDigits(s3))


