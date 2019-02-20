class Solution:
    def loudAndRich(self, richer, quiet):
        people = [[] for i in range(len(quiet))]
        for obs in richer: people[obs[1]].append(obs[0])

