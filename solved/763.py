class Solution:
    def partitionLabels(self, S):
        lastIndex = -1
        cur_sum = 0
        return_list = []
        aux_map = {}
        for i in range(0, len(S)):
            aux_map[S[i]] = i
        for i in range(0, len(S)):
            curLastIndex = aux_map[S[i]]
            if curLastIndex > lastIndex:
                lastIndex = curLastIndex
            if i == lastIndex:
                return_list.append(lastIndex + 1 - cur_sum)
                cur_sum = 1 + lastIndex
        return return_list


s = Solution()
S = "ababcbacadefegdehijhklij"
return_list = s.partitionLabels(S)
print (return_list)


























