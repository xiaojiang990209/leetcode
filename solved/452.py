class Solution:
    def findMinArrowShots(self, points):
        # No need to sort against the start coordinate.
        # Since we check the end coordinate of the current
        # interval with the start coordinate of as many proceeding
        # interval as we can: as long as the start coordinate is
        # smaller than the end coordinate, we dont care about the
        # start coordinate
        points.sort(key = lambda x: x[1])
        index = 0
        arrow = 0
        while index < len(points):
            # curMin = points[index][0]
            curMax = points[index][1]
            while index < len(points) and points[index][0] <= curMax:
                index += 1
            arrow += 1
        return arrow

sol = Solution()
points = [[1,10], [3,9], [4,11], [6,7], [6,9], [8,12], [9,12]]
print (sol.findMinArrowShots(points))
