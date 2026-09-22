class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        adj = [[] for _ in range(n)]
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))

        ways = [1] + [0] * (n - 1)
        path = [float('inf') for _ in range(n)]
        path[0] = 0
        q = [(0, 0)]

        res, shortest = 0, float('inf')
        while q:
            time, u = heapq.heappop(q)
            
            if time > path[u]:
                continue

            for v in adj[u]:
                if v[0] != u:
                    
                    if time + v[1] < path[v[0]]:
                        ways[v[0]] = ways[u]
                        path[v[0]] = time + v[1]
                        heapq.heappush(q, (path[v[0]], v[0]))
                    
                    elif time + v[1] == path[v[0]]:
                        ways[v[0]] = (ways[v[0]] + ways[u]) % MOD


        return ways[-1]