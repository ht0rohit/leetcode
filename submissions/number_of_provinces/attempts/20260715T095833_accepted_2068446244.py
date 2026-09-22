class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        q = collections.deque()

        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                visited.add(i)
                q.append(i)

                while q:
                    u = q.popleft()

                    for j in range(n):
                        if isConnected[u][j] == 1 and j not in visited:
                            visited.add(j)
                            q.append(j)

                if len(visited) == n:
                    break

        return count