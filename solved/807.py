class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row_max = [max(row) for row in grid]
        transpose = [[row[i] for row in grid] for i in range(len(grid))]
        col_max = [max(row) for row in transpose]
        sum_add = 0
        for i, row in enumerate(grid):
            for j, elem in enumerate(row):
                max_height = min(row_max[i], col_max[j])
                if elem < max_height:
                    sum_add = sum_add + max_height - elem

        return sum_add

grid = [[3, 0, 8, 4], [2,4,5,7], [9,2,6,3],[0,3,1,0]]
sol = Solution()
print (sol.maxIncreaseKeepingSkyline(grid))
