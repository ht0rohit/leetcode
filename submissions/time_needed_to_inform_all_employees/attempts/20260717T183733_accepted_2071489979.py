class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = [[] for _ in range(n)]
        for i in range(len(manager)):
            if manager[i] != -1:
                adj[manager[i]].append(i)

        q = collections.deque([(headID, informTime[headID])])
        maxtime = float('-inf')

        while q:
            u, t = q.popleft()
            maxtime = max(maxtime, t)

            for elem in adj[u]:
                q.append((elem, t + informTime[elem]))
                
        return maxtime