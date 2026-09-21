class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        adj = [set() for _ in range(n)]
        degree = [0] * n
        for elem in roads:
            adj[elem[0]].add(elem[1])
            adj[elem[1]].add(elem[0])
            degree[elem[0]] += 1
            degree[elem[1]] += 1

        maxRank = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = degree[i] + degree[j]
                if i in adj[j]:
                    rank -= 1
                maxRank = max(maxRank, rank)

        return maxRank