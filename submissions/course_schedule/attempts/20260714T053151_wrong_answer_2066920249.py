class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        for elem in prerequisites:
            adj[elem[1]].append(elem[0])

        visited = set()

        def dfs(u):
            nonlocal visited
            visited.add(u)

            for elem in adj[u]:
                if elem not in visited:
                    if dfs(elem):
                        return True
                else:
                    return True

            return False

        res = dfs(0)
        return True if not res else False