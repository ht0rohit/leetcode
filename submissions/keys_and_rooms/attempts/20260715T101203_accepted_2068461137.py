class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)

        visited = {0}
        q = collections.deque([0])

        while q:
            u = q.popleft()

            for i in range(len(rooms[u])):
                if rooms[u][i] not in visited:
                    visited.add(rooms[u][i])
                    q.append(rooms[u][i])

        if len(visited) == n:
            return True
        return False