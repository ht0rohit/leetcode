class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res, temp = [], []

        def dfs(u):
            temp.append(u)
            
            if u == n - 1:
                res.append(temp[:])
                return

            for elem in graph[u]:
                dfs(elem)
                temp.pop()

        dfs(0)
        return res