class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for i in range(numCourses)]
        for elem in prerequisites:
            adj[elem[1]].append(elem[0])
        n = len(adj)

        visited = set()
        recStack = set()
        res = []
        
        def dfs_cycle(u):
            visited.add(u)
            recStack.add(u)
            
            for elem in adj[u]:
                if elem not in visited:
                    if dfs_cycle(elem):
                        return True
                elif elem in recStack:
                    return True
            
            recStack.remove(u)
            res.append(u)
            return False

        for i in range(n):
            if i not in visited:
                if dfs_cycle(i):
                    return []

        return res[::-1]