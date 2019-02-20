import sys

class Solution:
    def subdomainVisits(self, cpdomains):
        pair_map = {}
        for cpdomain in cpdomains:
            pair = cpdomain.split(' ')
            temp = pair[1]
            for i in range(0, temp.count('.') + 1):
                if temp in pair_map:
                    pair_map[temp] = pair_map[temp] + int(pair[0])
                else:
                    pair_map[temp] = int(pair[0])
                if '.' in temp:
                    temp = temp[temp.index('.') + 1:]
        return_list = list(map(lambda v : ' '.join([str(v[1]), str(v[0])]), pair_map.items()))
        return return_list

cpdomains = ["9001 discuss.leetcode.com", "50 yahoo.com"]
print (Solution().subdomainVisits(cpdomains))
