class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1:
            return informTime[0]

        adj = [[] for _ in range(n)]
        for i in range(len(manager)):
            if manager[i] != -1:
                adj[manager[i]].append(i)

        visited = {headID}
        q = collections.deque([(headID, informTime[headID])])
        maxtime = float('-inf')

        while q:
            u, t = q.popleft()

            for elem in adj[u]:
                if elem not in visited:
                    visited.add(elem)
                    q.append((elem, t + informTime[elem]))
                    maxtime = max(maxtime, t + informTime[elem])

            if len(visited) == n:
                break
                
        return maxtime