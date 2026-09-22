class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = [[] for _ in range(n)]
        for elem in flights:
            adj[elem[0]].append((elem[1], elem[2]))

        price = [float('inf')] * n
        price[src] = 0
        heap = [(0, src, 0)]

        while heap:
            cost, u, stops = heapq.heappop(heap)
            
            if price[u] < cost:
                continue

            for v, w in adj[u]:
                if price[v] > price[u] + w:
                    if v != dst or (v == dst and stops <= k):
                        price[v] = price[u] + w
                        heapq.heappush(heap, (price[v], v, stops + 1))

        return price[dst] if price[dst] != float('inf') else -1
            