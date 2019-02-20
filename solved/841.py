class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def dfs(visited, rooms, n):
            for room in rooms[n]:
                if not visited[room]:
                    visited[room] = True
                    dfs(visited, rooms, room)

        N = len(rooms)
        visited = [False for i in range(N)]
        n = 0
        visited[n] = True
        dfs(visited, rooms, n)
        for visit in visited:
            if not visit: return False
        return True


rooms = [[1], [2], [3], []]
rooms2 = [[1,3], [3,0,1], [2], [0]]
sol = Solution()
print (sol.canVisitAllRooms(rooms))
print (sol.canVisitAllRooms(rooms2))
