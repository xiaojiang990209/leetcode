from random import *
class Solution:
    def __init__(self, nums):
        self.org = nums

    def reset(self):
        return self.org

    def shuffle(self):
        shuffled = self.org[:]
        length = len(shuffled)
        for i in range(length - 1):
            randIndex = randrange(i+1, length)
            temp = shuffled[i]
            shuffled[i] = shuffled[randIndex]
            shuffled[randIndex] = temp
        return shuffled

