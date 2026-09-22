class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        for elem in prerequisites:
            adj[elem[1]].append(elem[0])

        visited = set()
        q = collections.deque()
        res = False

        for i in range(len(adj)):

            if i not in visited:
                visited.add(i)
                q.append(i)

                while q:
                    u = q.popleft()

                    for elem in adj[u]:
                        if elem not in visited:
                            visited.add(elem)
                            q.append(elem)
                        else:
                            res = True
                            break
                            
                    if res:
                        break

                if len(visited) == len(adj) or res:
                    break
                    
        return True if not res else False
