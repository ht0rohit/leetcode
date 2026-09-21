class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        
        def helper(visited_helper, flag):
            while q:
                u = q.popleft()

                for v in adj[u]:
                    if flag and v in visited:
                        return list(range(n))
                    if v not in visited_helper:
                        visited_helper.add(v)
                        q.append(v)

            return []

        
        adj = [[] for _ in range(n)]
        for elem in invocations:
            adj[elem[0]].append(elem[1])

        visited = {k}
        q = collections.deque([k])

        helper(visited, 0)

        visited_copy = visited.copy()
        for i in range(n):
            if i not in visited_copy:
                visited_copy.add(i)
                q.append(i)

                res = helper(visited_copy, 1)
                if res:
                    return res

        return list(set(list(range(n))) - visited)
