class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for _ in range(numCourses)]
        for elem in prerequisites:
            adj[elem[0]].append(elem[1])

        res = []

        for source, target in queries:
            visited = {source}
            q = collections.deque([source])

            while q:
                u = q.popleft()
                
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
                        if v == target:
                            res.append(True)
                            break
                else:
                    continue
                break
            else:
                res.append(False)

        return res